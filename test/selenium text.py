from bs4 import BeautifulSoup
from selenium import webdriver
import selenium 
import time
# Create your driver
driver = webdriver.Firefox()

# Get a page
driver.get('http://www.psx.com.pk/')
# driver.find_element_by_css_selector('#Head > table > tbody > tr:nth-child(3) > td.linkText > div > table > tbody > tr > td:nth-child(1) > div > a:nth-child(3)').click()
driver.implicitly_wait(10)

# time.sleep(20) # delays for 5 seconds

# driver.find_element_by_xpath('//*[@id="Head"]/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[1]/div/a[3]').click()
# driver.find_element(By.CssSelector("#Head > table > tbody > tr:nth-child(3) > td.linkText > div > table > tbody > tr > td:nth-child(1) > div > a:nth-child(4)"))
# print(driver.text)
WebElement = driver.find_element_by_name('mainFrame')
print(WebElement.text)
driver.switch_to.frame(WebElement)

# # # driver.find_element_by_xpath('//*[@id="Head"]/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[1]/div/a[3]')
button = driver.find_element_by_xpath('//*[@id="Head"]/table/tbody/tr[3]/td[2]/div/table/tbody/tr/td[1]/div/a[3]').click()
# print(button.text)
driver.implicitly_wait(30)


# table1 = driver.find_element_by_xpath('//*[@id="contentdiv1"]/table/tbody/tr[2]/td[1]/table[2]/tbody/tr[4]/td/table[1]/tbody')
# Feed the source to BeautifulSoup
table1 = driver.find_element_by_xpath('//*[@id="contentdiv1"]/table/tbody/tr[2]/td[1]/table[2]/tbody/tr[4]/td')
soup = BeautifulSoup(table1.get_attribute('outerHTML'))

#print (soup)  # <title>Hacker News</title>
driver.implicitly_wait(10)

# Parsing data from each table
# table meta data
stockCatagory = ""
marketSummary = []
rowlist = []
tables = soup.find_all('tbody')
for tbody in tables:
	#print (tbody)
	rows = tbody.find_all('tr')
	stockCatagory = rows[0::]
	for tr in rows[2::]:
#		print(tr)
		rowsdata = tr.find_all('td')
		del rowlist
		rowlist = []
		for data in rowsdata:
			print(data.text)
		 	rowlist.append(data.text)
	 	marketSummary.append(rowlist)
		# print("...........")

print(marketSummary)




driver.quit() #PageContent_lblMiddle > table > tbody > tr:nth-child(2) > td > table:nth-child(3) > tbody > tr:nth-child(4) > td > table:nth-child(1) > tbody
