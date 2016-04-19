import numpy as np 
import mongo_data as mdata
import forexCal as fx
import schedule
import time
import easygui

def forexRoutine():
	pnumber = ""
	pnumber = easygui.enterbox(msg='Enter phone number:', title='Forex plotter ', default='03463565843', strip=True)
	print("Fetching stock data")
	namelist = mdata.getstockNameList()
	counter = 0

	#file to send as message
	

	for stockname in namelist:
		if counter == 5:
			break
		closep = mdata.getClosingRates(stockname)
		if len(closep) < 26:
			continue
		MA5  = fx.movingaverage(closep,5)
		MA10 = fx.movingaverage(closep,10)
		EMA7 = fx.ExpMovingAverage(closep,7)
		EMA10 = fx.ExpMovingAverage(closep,10)
		rsi = fx.rsiFunc(closep)
		macd = fx.computeMACD(closep)

		print('Stock Name: ' + stockname)
		print ('MA 5:')
		print(MA5)
		print ('MA 10:')
		print(MA10)
		print('EMA 7:')
		print(EMA7)
		print('EMA 10:')
		print(EMA10)

		print('RSI:')
		print(rsi)
		messagestr = "stock: "+ stockname 
		nl = "\n"
		# RSI calculation
		rsiarray = rsi.tolist()

		if rsiarray[len(rsiarray) -1] > 70:
			messagestr = messagestr + nl + "stock is Overbought"
			print('stock is Overbought')
		if rsiarray[len(rsiarray) -1] < 30 :
			messagestr = messagestr + nl + "stock is Oversold"
			print('stock is Oversold')
		

		print('MACD:')
		print(macd)
		
		# print(type(macd))
		macdres = macd[2]
		#macd calculations
		if macdres[len(macdres)-1] > 0:
			#time to sell bullish crossover 
			messagestr = messagestr + nl + "Time to buy this stock"
			print("Time to buy this stock")
		if macdres[len(macdres)-1] < 0:
			#time to buy  bearish crossover
			messagestr = messagestr + nl + "Time to sell this stock"
			print("Time to sell this stock")

		#message generation
		if messagestr == "stock: "+ stockname:
			print("no noticeable trend change")
		else:
		#favorable tread did appear
			mdata.createSMS(messagestr,pnumber)
			
		# counter+=1


# run the forex routine once every 24 hours
# 
# schedule.every().day.at("14:30").do(forexRoutine) #2:30 pm
# schedule.every(24).hours.do(forexRoutine)
# while True:
# 	try:
# 	schedule.run_pending()
# 		time.sleep(1)
# 	except Exception as e:
# 		print ("Exception occured: ", e)
forexRoutine()

