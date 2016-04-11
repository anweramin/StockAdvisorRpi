import pymongo

#closing rates
def getStockdata(stockSymbol):
	client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
	#connect to the rightDB in the cluster
	db = client['stockadvisordb']
	cursor = db.stocks.find()

	stockarry = []
	for document in cursor:
		date = str(document['date'].date())
		for st in document['stocks']:
			if st['SYMBOL'] == stockSymbol:
				st['date'] = date
				stockarry.append(st)

	# with open('testdata.txt', 'w') as the_file:
	# 	the_file.write(str(stockarry))
	# 	the_file.close()	
	
	return stockarry

def getClosingRates(stockSymbol):
	puredata = getStockdata(stockSymbol)
	closep = []
	for st in puredata:
		closep.append(st['LDCP'])
	# print (closep)
	return closep


# getClosingRates("Atlas Honda Ltd")
# stock = getStockdata("Atlas Honda Ltd")