param(
    [string]$OutputDirectory = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $OutputDirectory)) {
    New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}

$asOfDate = Get-Date
$period2 = [DateTimeOffset]::new($asOfDate.Date.AddDays(2)).ToUnixTimeSeconds()
$sourceTemplate = 'https://query1.finance.yahoo.com/v8/finance/chart/{0}?period1=0&period2={1}&interval=1d&events=div%2Csplits&includeAdjustedClose=true'

function Get-YahooAdjustedHistory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Ticker
    )

    $uri = $sourceTemplate -f $Ticker, $period2
    $response = Invoke-RestMethod -Uri $uri -Method Get

    if ($response.chart.error) {
        throw "Yahoo Finance returned an error for $Ticker`: $($response.chart.error.description)"
    }

    $result = $response.chart.result[0]
    $timestamps = @($result.timestamp)
    $quote = $result.indicators.quote[0]
    $adjusted = @($result.indicators.adjclose[0].adjclose)
    $rows = [System.Collections.Generic.List[object]]::new()

    for ($i = 0; $i -lt $timestamps.Count; $i++) {
        if ($null -eq $adjusted[$i]) {
            continue
        }

        $tradeDate = [DateTimeOffset]::FromUnixTimeSeconds([int64]$timestamps[$i]).UtcDateTime.Date
        $rows.Add([pscustomobject]@{
            Ticker   = $Ticker
            Date     = $tradeDate.ToString('yyyy-MM-dd')
            Open     = if ($null -eq $quote.open[$i]) { $null } else { [double]$quote.open[$i] }
            High     = if ($null -eq $quote.high[$i]) { $null } else { [double]$quote.high[$i] }
            Low      = if ($null -eq $quote.low[$i]) { $null } else { [double]$quote.low[$i] }
            Close    = if ($null -eq $quote.close[$i]) { $null } else { [double]$quote.close[$i] }
            AdjClose = [double]$adjusted[$i]
            Volume   = if ($null -eq $quote.volume[$i]) { $null } else { [long]$quote.volume[$i] }
        })
    }

    if ($rows.Count -eq 0) {
        throw "No adjusted-price observations were returned for $Ticker."
    }

    return [pscustomobject]@{
        Ticker       = $Ticker
        SourceUrl    = $uri
        Currency     = $result.meta.currency
        Exchange     = $result.meta.exchangeName
        FirstDate    = $rows[0].Date
        LastDate     = $rows[$rows.Count - 1].Date
        ObservationCount = $rows.Count
        Rows         = $rows
    }
}

function Get-YearEndRows {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Rows
    )

    $Rows |
        Group-Object { ([datetime]$_.Date).Year } |
        ForEach-Object {
            $last = $_.Group | Sort-Object Date | Select-Object -Last 1
            [pscustomobject]@{
                Year     = [int]$_.Name
                Date     = $last.Date
                AdjClose = [double]$last.AdjClose
                IsPartialYear = ([int]$_.Name -eq $asOfDate.Year)
            }
        } |
        Sort-Object Year
}

function Get-RollingRows {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Ticker,
        [Parameter(Mandatory = $true)]
        [object[]]$YearEndRows,
        [Parameter(Mandatory = $true)]
        [int]$StartYear,
        [Parameter(Mandatory = $true)]
        [int]$EndYear
    )

    $byYear = @{}
    foreach ($row in $YearEndRows) {
        $byYear[[int]$row.Year] = $row
    }

    $rolling = [System.Collections.Generic.List[object]]::new()
    for ($year = $StartYear; $year -le ($EndYear - 5); $year++) {
        if (-not $byYear.ContainsKey($year) -or -not $byYear.ContainsKey($year + 5)) {
            continue
        }

        $start = $byYear[$year]
        $end = $byYear[$year + 5]
        $startDate = [datetime]$start.Date
        $endDate = [datetime]$end.Date
        $actualYears = ($endDate - $startDate).TotalDays / 365.2425
        $totalReturn = ([double]$end.AdjClose / [double]$start.AdjClose) - 1
        $cagr = [math]::Pow(([double]$end.AdjClose / [double]$start.AdjClose), (1 / $actualYears)) - 1

        $rolling.Add([pscustomobject]@{
            Ticker      = $Ticker
            StartYear   = $year
            EndYear     = $year + 5
            StartDate   = $start.Date
            EndDate     = $end.Date
            StartAdjClose = [double]$start.AdjClose
            EndAdjClose = [double]$end.AdjClose
            ActualYears = $actualYears
            TotalReturn = $totalReturn
            CAGR        = $cagr
            Status      = if ($end.IsPartialYear) { "Partial through $($end.Date)" } else { 'Complete 5-year window' }
        })
    }

    return $rolling
}

$histories = @{}
$yearEnds = @{}

foreach ($ticker in @('SPY', 'QQQ')) {
    $history = Get-YahooAdjustedHistory -Ticker $ticker
    $histories[$ticker] = $history
    $yearEnds[$ticker] = @(Get-YearEndRows -Rows $history.Rows)
    $history.Rows | Export-Csv -LiteralPath (Join-Path $OutputDirectory "$($ticker)_daily_adjusted.csv") -NoTypeInformation -Encoding UTF8
}

$allYears = ($yearEnds.Values | ForEach-Object { $_.Year } | Sort-Object -Unique)
$yearEndTable = foreach ($year in $allYears) {
    $spy = $yearEnds['SPY'] | Where-Object Year -eq $year | Select-Object -First 1
    $qqq = $yearEnds['QQQ'] | Where-Object Year -eq $year | Select-Object -First 1
    [pscustomobject]@{
        Year        = [int]$year
        SPY_Date    = if ($spy) { $spy.Date } else { $null }
        SPY_AdjClose = if ($spy) { [double]$spy.AdjClose } else { $null }
        QQQ_Date    = if ($qqq) { $qqq.Date } else { $null }
        QQQ_AdjClose = if ($qqq) { [double]$qqq.AdjClose } else { $null }
        IsPartialYear = ($year -eq $asOfDate.Year)
    }
}
$yearEndTable | Export-Csv -LiteralPath (Join-Path $OutputDirectory 'year_end_adjusted_prices.csv') -NoTypeInformation -Encoding UTF8

$currentYear = $asOfDate.Year
$rolling30 = @(
    Get-RollingRows -Ticker 'SPY' -YearEndRows $yearEnds['SPY'] -StartYear ($currentYear - 30) -EndYear $currentYear
    Get-RollingRows -Ticker 'QQQ' -YearEndRows $yearEnds['QQQ'] -StartYear ($currentYear - 30) -EndYear $currentYear
)
$rolling2008 = @(
    Get-RollingRows -Ticker 'SPY' -YearEndRows $yearEnds['SPY'] -StartYear 2008 -EndYear $currentYear
    Get-RollingRows -Ticker 'QQQ' -YearEndRows $yearEnds['QQQ'] -StartYear 2008 -EndYear $currentYear
)

$rolling30 | Export-Csv -LiteralPath (Join-Path $OutputDirectory 'rolling_5y_last_30_years.csv') -NoTypeInformation -Encoding UTF8
$rolling2008 | Export-Csv -LiteralPath (Join-Path $OutputDirectory 'rolling_5y_2008_to_2026.csv') -NoTypeInformation -Encoding UTF8

function Get-Stats {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Rows
    )

    $complete = @($Rows | Where-Object Status -eq 'Complete 5-year window')
    $all = @($Rows)
    $latest = $all | Sort-Object EndYear, EndDate | Select-Object -Last 1
    $sortedTotalReturns = @($complete | Sort-Object TotalReturn | ForEach-Object { [double]$_.TotalReturn })
    $sortedCagrs = @($complete | Sort-Object CAGR | ForEach-Object { [double]$_.CAGR })
    function Get-Median {
        param([double[]]$Values)
        if ($Values.Count -eq 0) { return $null }
        $middle = [math]::Floor($Values.Count / 2)
        if ($Values.Count % 2) { return $Values[$middle] }
        return ($Values[$middle - 1] + $Values[$middle]) / 2
    }
    return [pscustomobject]@{
        CompleteWindowCount = $complete.Count
        AverageTotalReturn = if ($complete.Count) { ($complete | Measure-Object TotalReturn -Average).Average } else { $null }
        MedianTotalReturn = Get-Median -Values $sortedTotalReturns
        AverageCAGR = if ($complete.Count) { ($complete | Measure-Object CAGR -Average).Average } else { $null }
        MedianCAGR = Get-Median -Values $sortedCagrs
        MinimumTotalReturn = if ($complete.Count) { ($complete | Measure-Object TotalReturn -Minimum).Minimum } else { $null }
        MaximumTotalReturn = if ($complete.Count) { ($complete | Measure-Object TotalReturn -Maximum).Maximum } else { $null }
        LatestWindow = $latest
    }
}

function Get-OverallReturn {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Rows,
        [datetime]$StartOnOrAfter
    )

    $eligible = if ($PSBoundParameters.ContainsKey('StartOnOrAfter')) {
        @($Rows | Where-Object { [datetime]$_.Date -ge $StartOnOrAfter })
    } else {
        @($Rows)
    }
    $start = $eligible | Sort-Object Date | Select-Object -First 1
    $end = $Rows | Sort-Object Date | Select-Object -Last 1
    $actualYears = (([datetime]$end.Date) - ([datetime]$start.Date)).TotalDays / 365.2425
    $totalReturn = ([double]$end.AdjClose / [double]$start.AdjClose) - 1
    [pscustomobject]@{
        StartDate = $start.Date
        EndDate = $end.Date
        StartAdjClose = [double]$start.AdjClose
        EndAdjClose = [double]$end.AdjClose
        ActualYears = $actualYears
        TotalReturn = $totalReturn
        CAGR = [math]::Pow(([double]$end.AdjClose / [double]$start.AdjClose), (1 / $actualYears)) - 1
    }
}

$summary = [ordered]@{
    GeneratedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')
    Method = 'Year-end to year-end using Yahoo Finance adjusted close; 2026 uses the latest available trading day.'
    YahooAdjustedCloseDefinition = 'Adjusted for applicable splits and dividend distributions.'
    SourceHelpUrl = 'https://help.yahoo.com/kb/SLN28256.html'
    SPY = [ordered]@{
        FirstDate = $histories['SPY'].FirstDate
        LastDate = $histories['SPY'].LastDate
        ObservationCount = $histories['SPY'].ObservationCount
        SourceUrl = $histories['SPY'].SourceUrl
        OverallPeriod = Get-OverallReturn -Rows $histories['SPY'].Rows -StartOnOrAfter $asOfDate.Date.AddYears(-30)
        Rolling30YearStats = Get-Stats -Rows @($rolling30 | Where-Object Ticker -eq 'SPY')
        RollingSince2008Stats = Get-Stats -Rows @($rolling2008 | Where-Object Ticker -eq 'SPY')
    }
    QQQ = [ordered]@{
        FirstDate = $histories['QQQ'].FirstDate
        LastDate = $histories['QQQ'].LastDate
        ObservationCount = $histories['QQQ'].ObservationCount
        SourceUrl = $histories['QQQ'].SourceUrl
        OverallPeriod = Get-OverallReturn -Rows $histories['QQQ'].Rows
        Rolling30YearStats = Get-Stats -Rows @($rolling30 | Where-Object Ticker -eq 'QQQ')
        RollingSince2008Stats = Get-Stats -Rows @($rolling2008 | Where-Object Ticker -eq 'QQQ')
    }
}

$summary | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $OutputDirectory 'analysis_snapshot.json') -Encoding UTF8

$manifest = [ordered]@{
    Files = @(
        'SPY_daily_adjusted.csv'
        'QQQ_daily_adjusted.csv'
        'year_end_adjusted_prices.csv'
        'rolling_5y_last_30_years.csv'
        'rolling_5y_2008_to_2026.csv'
        'analysis_snapshot.json'
    )
    GeneratedAt = $summary.GeneratedAt
    Notes = @(
        'QQQ began trading in 1999, so a full 30-year QQQ history does not exist.'
        '2026 observations are year-to-date through the latest available trading day.'
        'All return calculations use adjusted close to incorporate splits and distributions.'
    )
}
$manifest | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $OutputDirectory 'data_manifest.json') -Encoding UTF8

Write-Output ($summary | ConvertTo-Json -Depth 8)
