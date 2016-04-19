mongoexport -h ds015919.mlab.com:15919 -d stockadvisordb -c stocks -u stockadvisor -p anwer123 -o stock.json 

 mongo ds015919.mlab.com:15919/stockadvisordb -u stockadvisor -p anwer123


 db.copyDatabase(stockadvisordb, stockadvisordblocal, ds015919.mlab.com:15919, stockadvisor, anwer123, SCRAM-SHA-1)

db.copyDatabase("stockadvisordb", "stockadvisordblocal", "ds015919.mlab.com:15919", "stockadvisor", "anwer123", "SCRAM
-SHA-1");