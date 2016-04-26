import schedule
import time
import datetime

def job():
	d=datetime.datetime.now()
	if d.hour in range(9,23) and d.isoweekday:
		print("I'm working...")

# schedule.every(1).minutes.do(job)
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)