import ystockquote as ys

print(ys.get_price('TSLA'))
print(ys.get_historical_prices('GOOG', '2013-01-03', '2013-01-08'))
