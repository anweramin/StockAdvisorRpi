import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler("~/Desktop/Embedded Project/stocks.log")
logger.info('STARING SCRAPING')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 

logger.setLevel(logging.WARNING)
logger.info('STARING SCRAPING')
logger.info('STARING SCRAPING')
logger.info('STARING SCRAPING')
logger.info('STARING SCRAPING')

