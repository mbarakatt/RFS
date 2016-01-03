
import numpy as np
import sys
from datetime import datetime




CLOSING_PRICE = 3
start_date = "5-Jan-10"
# start_date = "4-Jan-05"
end_date = "31-Dec-14"


# Load list of stocks
list_symbols = [l.split('.')[0] for l in open('../data/really-good-stocks.txt','r') ]

stock_data = {}
# Load stock data
for s in list_symbols:
	with open('../data/stocks/%s.csv' % s, 'r') as f:
		file_data = dict( (l.split(',')[0],l.split(',')[1:]) for l in  f.read().split('\n'))

	if start_date in file_data and float(file_data[start_date][CLOSING_PRICE]) > 0. :
		stock_data[s] = file_data



print("Total number of symbol avail on %s: %d" % (start_date, len(stock_data)))





def interval_in_years(start, end):
	return (datetime.strptime(end, '%d-%b-%y') - datetime.strptime(start, '%d-%b-%y')).days / 365.24


def variance_with_n(n, seed):
	np.random.seed(seed=seed)
# Filter
# subset_list_symbols = np.random.choice(stock_data.keys(), len(stock_data) )
	subset_list_symbols = np.random.choice(stock_data.keys(), n)

	start_prices = []
	end_prices = []
	# print subset_list_symbols
	for s in subset_list_symbols:
		start_prices.append(float(stock_data[s][start_date][CLOSING_PRICE]))
		try:
			end_prices.append(float(stock_data[s][end_date][CLOSING_PRICE]))
		except KeyError:
			end_prices.append(0.0)


	start_prices = np.array(start_prices)
	end_prices = np.array(end_prices)
	# print start_prices, (np.sum(end_prices/start_prices) - n) / n/ interval_in_years(start_date,end_date)

	return (np.sum(end_prices/start_prices) - n) / n / interval_in_years(start_date,end_date)








interest_rates = np.zeros(((600) / 5, 300))
for j, n in enumerate(range(1, 601, 5)):
	print("n: %d " % j)
	for i in range(300):
		interest_rates[j,i] = variance_with_n(n, seed=i*j)

np.savetxt('./interest_rates.txt', interest_rates)
