import pymongo
import numpy as np 
import datetime
# getall metadata for a stock.
def getStockdata(stockSymbol):
	client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
	#connect to the rightDB in the cluster
	db = client['stockadvisordb']
	cursor = db.stocks.find().sort('date',pymongo.ASCENDING)

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

#closing rates
def getClosingRates(stockSymbol):
	puredata = getStockdata(stockSymbol)
	closep = []
	for st in puredata:
		closep.append(float(st['LDCP']))
	# print (closep)
	closep = np.asarray(closep)	
	return closep

def uiFeed(stockSymbol):
	puredata = getStockdata(stockSymbol)
	# print(puredata)
	stockdata = []
	for st in puredata:
		strpdate = st["date"].replace("-","")
		volume = st["VOLUME"].replace(",","")
		#values:Date,close,high,low,open,volume
		setdata = strpdate + "," +st["LDCP"] + "," + st["HIGH"] + "," + st["LOW"] + "," + st["OPEN"] + "," + volume
		# print(setdata)
		stockdata.append(setdata)
	return stockdata

def getstockNameList() :
	client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
	#connect to the rightDB in the cluster
	db = client['stockadvisordb']
	cursor = db.stocks.find()
	namelist = []
	size = cursor.count() - 1
	doc = cursor[size]
	for rec in doc['stocks']:
		name = rec['SYMBOL']
		namelist.append(name)
	# print(namelist)
	return namelist

def createSMS(messagebody):
	# messagetext = "Some text to check  " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#connection the the mlab cloud
	client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
	#connect to the rightDB in the cluster
	db = client['stockadvisordb']
	#the stocks object to be inserted
	post = {
	   
    	"body" : messagebody,
    	"sent_flag" : False,
    	"to" : "03463565843",
		"date": datetime.datetime.now()
		}
	#get table name, this is only for simplfication for reuse
	stocks = db.notifications
	#perfrom insert operations
	stock_id = stocks.insert_one(post).inserted_id
	print(stock_id)


def getStocktest(stockSymbol):
	client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
	#connect to the rightDB in the cluster
	db = client['stockadvisordb']
	cursor = db.stocks.find().sort('date',pymongo.ASCENDING)

	stockarry = []
	for document in cursor:
		print(document['date'].date())	

	# with open('testdata.txt', 'w') as the_file:
	# 	the_file.write(str(stockarry))
	# 	the_file.close()	
	

# getClosingRates("Atlas Honda Ltd")
# stock = getStockdata("Atlas Honda Ltd")
# getstockNameList()
# 
# getStocktest("Atlas Honda Ltd")
# uiFeed("Atlas Honda Ltd")