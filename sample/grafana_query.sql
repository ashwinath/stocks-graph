SELECT
  time_bucket('1 day', time) as time,
  symbol,
  avg(price) as price
FROM stocks_history
WHERE
  $__timeFilter(time)
GROUP BY time, symbol
ORDER BY time;
