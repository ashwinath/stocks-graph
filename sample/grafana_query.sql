-- NAV
SELECT
  time_bucket('1 day', time) as time,
  symbol,
  avg(nav) as nav
FROM stats
WHERE
  $__timeFilter(time)
GROUP BY time, symbol
ORDER BY time;

-- Principal vs NAV
SELECT
  time_bucket('1 day', time) as time,
  sum(nav) as nav,
  sum(principal) as principal
FROM stats
WHERE
  $__timeFilter(time)
GROUP BY time
ORDER BY time;

-- Returns
SELECT
  time_bucket('1 day', time) as time,
  symbol,
  avg(returns_percentage) as returns
FROM stats
WHERE
  $__timeFilter(time)
GROUP BY time, symbol
ORDER BY time;

-- Portfolio Returns
SELECT
  time_bucket('1 day', time) as time,
  (sum(nav) - sum(principal)) / sum(principal) as returns
FROM stats
WHERE
  $__timeFilter(time)
GROUP BY time
ORDER BY time


-- Piechart on Portfolio
SELECT 
    time_bucket('1 day', time) as time,
    symbol,
    sum(nav) as nav
FROM stats
WHERE
    time=DATE_TRUNC('day', CURRENT_TIMESTAMP - INTERVAL '1 day')
GROUP BY time, symbol
