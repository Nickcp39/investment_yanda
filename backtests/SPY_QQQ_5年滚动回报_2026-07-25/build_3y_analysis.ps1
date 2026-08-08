$ErrorActionPreference = 'Stop'
$base = $PSScriptRoot
$yearEndRows = Import-Csv -LiteralPath (Join-Path $base 'year_end_adjusted_prices.csv')

function Get-Median {
    param([double[]]$Values)
    if ($Values.Count -eq 0) { return $null }
    $sorted = @($Values | Sort-Object)
    $middle = [math]::Floor($sorted.Count / 2)
    if ($sorted.Count % 2) { return $sorted[$middle] }
    return ($sorted[$middle - 1] + $sorted[$middle]) / 2
}

function Get-ThreeYearRows {
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
    for ($year = $StartYear; $year -le ($EndYear - 3); $year++) {
        if (-not $byYear.ContainsKey($year) -or -not $byYear.ContainsKey($year + 3)) { continue }
        $start = $byYear[$year]
        $end = $byYear[$year + 3]
        $startDate = [datetime]$start.$dateColumn
        $endDate = [datetime]$end.$dateColumn
        $years = ($endDate - $startDate).TotalDays / 365.2425
        $ratio = [double]$end.$priceColumn / [double]$start.$priceColumn
        $result.Add([pscustomobject]@{
            Ticker = $Ticker
            StartYear = $year
            EndYear = $year + 3
            StartDate = $start.$dateColumn
            EndDate = $end.$dateColumn
            StartAdjClose = [double]$start.$priceColumn
            EndAdjClose = [double]$end.$priceColumn
            ActualYears = $years
            TotalReturn = $ratio - 1
            CAGR = [math]::Pow($ratio, 1 / $years) - 1
            Status = if ([bool]::Parse($end.IsPartialYear)) { "Partial through $($end.$dateColumn)" } else { 'Complete 3-year window' }
        })
    }
    return $result
}

function Get-Stats {
    param([object[]]$Rows)
    $complete = @($Rows | Where-Object Status -eq 'Complete 3-year window')
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
$rolling2008 = @(
    Get-ThreeYearRows -Ticker 'SPY' -StartYear 2008 -EndYear $currentYear
    Get-ThreeYearRows -Ticker 'QQQ' -StartYear 2008 -EndYear $currentYear
)
$rollingHistory = @(
    Get-ThreeYearRows -Ticker 'SPY' -StartYear ($currentYear - 30) -EndYear $currentYear
    Get-ThreeYearRows -Ticker 'QQQ' -StartYear 1999 -EndYear $currentYear
)

$rolling2008 | Export-Csv -LiteralPath (Join-Path $base 'rolling_3y_2008_to_2026.csv') -NoTypeInformation -Encoding UTF8
$rollingHistory | Export-Csv -LiteralPath (Join-Path $base 'rolling_3y_history.csv') -NoTypeInformation -Encoding UTF8

$snapshot = [ordered]@{
    GeneratedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')
    DataThrough = '2026-07-24'
    WindowYears = 3
    Method = 'Year-end to year-end using Yahoo Finance adjusted close; 2026 uses latest available trading day.'
    SPY = [ordered]@{
        History = Get-Stats @($rollingHistory | Where-Object Ticker -eq 'SPY')
        Since2008 = Get-Stats @($rolling2008 | Where-Object Ticker -eq 'SPY')
    }
    QQQ = [ordered]@{
        History = Get-Stats @($rollingHistory | Where-Object Ticker -eq 'QQQ')
        Since2008 = Get-Stats @($rolling2008 | Where-Object Ticker -eq 'QQQ')
    }
}
$snapshot | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $base 'analysis_3y_snapshot.json') -Encoding UTF8
$snapshot | ConvertTo-Json -Depth 8
