#StockAdvisorRpi
> ```                                                             
 _____ _             _     ___      _       _               ______       _ 
/  ___| |           | |   / _ \    | |     (_)              | ___ \     (_)
\ `--.| |_ ___   ___| | _/ /_\ \ __| |_   ___ ___  ___  _ __| |_/ /_ __  _ 
 `--. \ __/ _ \ / __| |/ /  _  |/ _` \ \ / / / __|/ _ \| '__|    /| '_ \| |
/\__/ / || (_) | (__|   <| | | | (_| |\ V /| \__ \ (_) | |  | |\ \| |_) | |
\____/ \__\___/ \___|_|\_\_| |_/\__,_| \_/ |_|___/\___/|_|  \_| \_| .__/|_|
                                                                  | |      
                                                                  |_|      
> ```                                                                          
A raspberry pi based stock advisor.


## Table of Contents
* [Installation instuctions](#installation-instuctions)
* [Folder disctriptions](#folder-disctriptions)
* [File discriptions](#file-disctriptions)

##Installation instuctions       

Install Python3
	.. Remember selection box to add python to PATH env variables
	..	install pip installer for python packages
open cmd
run commands:
```bash
sudo apt-get install python3-pip
pip install selenium
pip install beautifulsoup4
pip install pymongo
pip install pytz
pip install datetime
pip install tzlocal
```


##Folder disctriptions    
>> \src 		 --			Source code for the project.


##File disctriptions        
> ``` 
>>scrapping_deamon   --         main logic for the scraping routine
>>systemlog.log      --         Log for all activites
>>Deamon.py          -- 		DEPRICATED::Containes the main logic for the scraping routine
>>stocks.log         -- 		DEPRICATED::Log for all activites
>>stockData.txt      --			DEPRICATED::temp data dump at the end of activies. 
> ``` 




