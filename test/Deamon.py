from bs4 import BeautifulSoup
from selenium import webdriver
import selenium 
import time
import logging


## logging for checking repeated task status and timing
logger = logging.getLogger("__StockAsst.__")
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('stocks.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
#logger.setLevel(logging.WARNING)

def scraping():
	logger.info('STARING SCRAPING')
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
	tables = soup.find_all('tbody')
	for tbody in tables:
		rows = tbody.find_all('tr')
		stockCatagory = rows[0::]
		for tr in rows[2::]:
			rowsdata = tr.find_all('td')
			del rowlist
			rowlist = []
			for data in rowsdata:
				#print(data.text)
			 	rowlist.append(data.text)
			marketSummary.append(rowlist)
	#print(marketSummary)
	driver.quit()
	logger.info('DATA RETRIVED') 
	return marketSummary
count = 5
while 1:
	if count == 0:
		break
	marketsummary =scraping()
	print(marketsummary)
	print("Script ending")	
	time.sleep(100)
	--count
