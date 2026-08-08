$ErrorActionPreference = 'Stop'

$base = $PSScriptRoot
$windowYears = 10
$dataThrough = '2026-07-24'
$yearEndRows = Import-Csv -LiteralPath (Join-Path $base 'year_end_adjusted_prices.csv')

function Get-Median {
    param([double[]]$Values)
    if ($Values.Count -eq 0) { return $null }
    $sorted = @($Values | Sort-Object)
    $middle = [math]::Floor($sorted.Count / 2)
    if ($sorted.Count % 2) { return $sorted[$middle] }
    return ($sorted[$middle - 1] + $sorted[$middle]) / 2
}

function Get-RollingRows {
    param([string]$Ticker, [int]$StartYear, [int]$EndYear)

    $dateColumn = "${Ticker}_Date"
    $priceColumn = "${Ticker}_AdjClose"
    $byYear = @{}
    foreach ($row in $yearEndRows) {
        if ($row.$dateColumn -and $row.$priceColumn) {
            $byYear[[int]$row.Year] = $row
        }
    }

    $result = [System.Collections.Generic.List[object]]::new()
    for ($year = $StartYear; $year -le ($EndYear - $windowYears); $year++) {
        if (-not $byYear.ContainsKey($year) -or -not $byYear.ContainsKey($year + $windowYears)) { continue }
        $start = $byYear[$year]
        $end = $byYear[$year + $windowYears]
        $startDate = [datetime]$start.$dateColumn
        $endDate = [datetime]$end.$dateColumn
        $actualYears = ($endDate - $startDate).TotalDays / 365.2425
        $ratio = [double]$end.$priceColumn / [double]$start.$priceColumn
        $isPartial = [bool]::Parse($end.IsPartialYear)

        $result.Add([pscustomobject]@{
            Ticker = $Ticker
            StartYear = $year
            EndYear = $year + $windowYears
            StartDate = $start.$dateColumn
            EndDate = $end.$dateColumn
            StartAdjClose = [double]$start.$priceColumn
            EndAdjClose = [double]$end.$priceColumn
            ActualYears = $actualYears
            TotalReturn = $ratio - 1
            CAGR = [math]::Pow($ratio, 1 / $actualYears) - 1
            Status = if ($isPartial) { "Partial through $($end.$dateColumn)" } else { "Complete $windowYears-year window" }
        })
    }
    return $result
}

function Get-Stats {
    param([object[]]$Rows)
    $complete = @($Rows | Where-Object Status -eq "Complete $windowYears-year window")
    $returns = [double[]]@($complete | ForEach-Object TotalReturn)
    $cagrs = [double[]]@($complete | ForEach-Object CAGR)
    [pscustomobject]@{
        CompleteWindowCount = $complete.Count
        AverageTotalReturn = ($returns | Measure-Object -Average).Average
        MedianTotalReturn = Get-Median $returns
        MinimumTotalReturn = ($returns | Measure-Object -Minimum).Minimum
        MaximumTotalReturn = ($returns | Measure-Object -Maximum).Maximum
        AverageCAGR = ($cagrs | Measure-Object -Average).Average
        MedianCAGR = Get-Median $cagrs
        LatestCompleteWindow = $complete | Sort-Object EndYear | Select-Object -Last 1
        CurrentPartialWindow = $Rows | Where-Object Status -like 'Partial*' | Sort-Object EndYear | Select-Object -Last 1
    }
}

$currentYear = 2026
$rollingSince2008 = @(
    Get-RollingRows -Ticker 'SPY' -StartYear 2008 -EndYear $currentYear
    Get-RollingRows -Ticker 'QQQ' -StartYear 2008 -EndYear $currentYear
)
$rollingHistory = @(
    Get-RollingRows -Ticker 'SPY' -StartYear ($currentYear - 30) -EndYear $currentYear
    Get-RollingRows -Ticker 'QQQ' -StartYear 1999 -EndYear $currentYear
)

$rollingSince2008 | Export-Csv -LiteralPath (Join-Path $base 'rolling_10y_2008_to_2026.csv') -NoTypeInformation -Encoding UTF8
$rollingHistory | Export-Csv -LiteralPath (Join-Path $base 'rolling_10y_history.csv') -NoTypeInformation -Encoding UTF8

$snapshot = [ordered]@{
    GeneratedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')
    DataThrough = $dataThrough
    WindowYears = $windowYears
    Method = 'Year-end to year-end using Yahoo Finance adjusted close; 2026 uses latest available trading day.'
    SPY = [ordered]@{
        History = Get-Stats @($rollingHistory | Where-Object Ticker -eq 'SPY')
        Since2008 = Get-Stats @($rollingSince2008 | Where-Object Ticker -eq 'SPY')
    }
    QQQ = [ordered]@{
        History = Get-Stats @($rollingHistory | Where-Object Ticker -eq 'QQQ')
        Since2008 = Get-Stats @($rollingSince2008 | Where-Object Ticker -eq 'QQQ')
    }
}

$snapshot | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $base 'analysis_10y_snapshot.json') -Encoding UTF8
$snapshot | ConvertTo-Json -Depth 8
