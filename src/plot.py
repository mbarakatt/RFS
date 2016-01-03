import matplotlib.pylab as plt
import seaborn
import numpy as np
import matplotlib.mlab as mlab

interest_rates = np.loadtxt('./interest_rates.txt')

plt.plot((np.array(range(interest_rates.shape[0]))+1)[10:], np.std(interest_rates, axis=1)[10:])
plt.title('Variance interest rate vs Number symbols')
plt.xlabel('Number of symbols')
plt.ylabel('Variance of interest rates')
plt.savefig('variance.pdf')



plt.figure()
for i in range( interest_rates.shape[0]):
	plt.plot([(np.array(range(interest_rates.shape[0]))+1)[i]] * interest_rates.shape[1], interest_rates[i,:] , 'o', alpha=0.2)
plt.plot(np.array(range(interest_rates.shape[0]))+1, np.mean(interest_rates, axis=1))

plt.ylim(0,1)
plt.savefig('mean.pdf')



for i in range(interest_rates.shape[0]):
	plt.figure()
	n, bins, patches = plt.hist(interest_rates[i,:], 30, normed=1, facecolor='green', alpha=0.75)

	mu = np.mean(interest_rates[i,:])
	sigma = np.std(interest_rates[i,:])
	# add a 'best fit' line
	y = mlab.normpdf( bins, mu, sigma)
	l = plt.plot(bins, y, 'r--', linewidth=1)

	plt.savefig('%03d.pdf' % i )
	plt.close()
