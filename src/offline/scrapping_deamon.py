from bs4 import BeautifulSoup
from selenium import webdriver
import selenium 
import time
# import logging
# import simpleJson as json
import pymongo
import datetime
import tzlocal
# import pytz

# ## logging for checking repeated task status and timing
# logger = logging.getLogger("__StockAsst.__")
# logger.setLevel(logging.INFO)
# # create a file handler
# handler = logging.FileHandler('systemlog.log')
# handler.setLevel(logging.INFO)
# # create a logging format
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# # add the handlers to the logger
# logger.addHandler(handler)
# #logger.setLevel(logging.WARNING)

def scraping():
	# logger.info('STARING SCRAPING')
	driver = webdriver.Firefox()
	driver.get('http://www.psx.com.pk/')
	driver.implicitly_wait(10)
	WebElement = driver.find_element_by_name('mainFrame')
	print(WebElement.text)
	driver.switch_to.frame(WebElement)
	button = driver.find_element_by_xpath('//*[@id="Head"]/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[1]/div/a[3]').click()
	driver.implicitly_wait(30)
	table1 = driver.find_element_by_xpath('//*[@id="contentdiv1"]/table/tbody/tr[2]/td[1]/table[2]/tbody/tr[4]/td')
	soup = BeautifulSoup(table1.get_attribute('outerHTML'))
	driver.implicitly_wait(10)
	stockCatagory = ""
	marketSummary = []
	rowlist = []
	title_arry = ["SYMBOL" ,"LDCP", "OPEN" ,"HIGH" ,"LOW", "CURRENT", "CHANGE", "VOLUME"]

	tables = soup.find_all('tbody')
	for tbody in tables:
		rows = tbody.find_all('tr')
		stockCatagory = rows[0::]
		for tr in rows[2::]:
			rowsdata = tr.find_all('td')
			del rowlist
			rowlist = []
			json_obj = {}
			counter = 0
			symcnt = 0
			for data in rowsdata:
				#print(data.text)
				if symcnt == 0:
					sym = data.text
					symcnt = 1
				json_obj[title_arry[counter]] = data.text
				counter += 1
			# json_obj2 = {}
			# json_obj2[sym] = json_obj 
			marketSummary.append(json_obj)
	print(marketSummary)
	driver.quit()
	# logger.info('DATA RETRIVED') 
	return marketSummary
# test loop
# count = 5
# while 1:
# 	if count == 0:
# 		break
# 	marketsummary =scraping()
# 	print(marketsummary)
# 	print("Script ending")	
# 	time.sleep(100)
# 	--count

#Simply prints the scrapped data.
marketsummary =scraping()

#Get stocks before db ops to ensure no extra delay

###################################
#=======DataBase ops==============
###################################


#connection the the mlab cloud
client = pymongo.MongoClient('mongodb://localhost:27018/')
#connect to the rightDB in the cluster
db = client['stockadvisordblocal']
#the stocks object to be inserted
post = {
	   "stocks": marketsummary,
	   "date": datetime.datetime.now()}
#get table name, this is only for simplfication for reuse
stocks = db.stocks
#perfrom insert operations
stock_id = stocks.insert_one(post).inserted_id
print(stock_id)
#log operation
# logger.info('Stock record added to DB')
