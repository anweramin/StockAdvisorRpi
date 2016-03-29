import logging
import json
import pymongo
import datetime

## logging for checking repeated task status and timing
logger = logging.getLogger("__StockAsst.__")
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('systemlog.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
#logger.setLevel(logging.WARNING)



# Add a notification.
messagetext = "Some text"

#connection the the mlab cloud
client = pymongo.MongoClient('mongodb://stockadvisor:anwer123@ds015919.mlab.com:15919/stockadvisordb?authMechanism=SCRAM-SHA-1')
#connect to the rightDB in the cluster
db = client['stockadvisordb']
#the stocks object to be inserted
post = {
	   
    "body" : messagetext,
    "sent_flag" : "false",
    "to" : "03463565843",
	"date": datetime.datetime.now()
	}
#get table name, this is only for simplfication for reuse
stocks = db.notifications
#perfrom insert operations
stock_id = stocks.insert_one(post).inserted_id
print(stock_id)
#log operation
logger.info('Notification record added to DB')
