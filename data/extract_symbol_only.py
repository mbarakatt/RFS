
f = open('companylist.csv', 'r')

f.readline()
for line in f:
	print line.split(',')[0].replace('"','')
