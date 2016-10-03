from scraper import HackerNewsParser
import time
import logging

if __name__ == "__main__":

    logging.basicConfig(filename='running.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')


    hackerNewsParser = HackerNewsParser('https://news.ycombinator.com/')

    try:
        hackerNewsParser.get_itemlist()
    except Exception as exc:
        print('exception')
        logging.exception("Error with the scrapin")
        raise
    else:
        logging.info("{}: Finished scraping".format(time.ctime()))
        print('success')


