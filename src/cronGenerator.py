from crontab import CronTab

# empty_cron    = CronTab()
# my_user_cron  = CronTab(user=True)
users_cron    = CronTab(user=True)
# will need to change like on deployment.
job  = cron.new(command='python3 /home/anweramin/Desktop/Git repo/StockAdvisorRpi/src/scrapping_deamon.py')
