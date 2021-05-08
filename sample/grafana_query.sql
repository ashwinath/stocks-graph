SELECT
  time_bucket('1 day', time) as time,
  symbol,
  avg(nav) as nav,
  avg(principal) as principal,
  avg(returns_percentage) as returns,
FROM stats
WHERE
  $__timeFilter(time)
GROUP BY time, symbol
ORDER BY time
