import threading
import requests
import time
from bs4 import BeautifulSoup
from lxml import html
import random

class YahooFinanceWorker(threading.Thread):
    def __init__(self,symbol,**kwargs):
        super(YahooFinanceWorker,self).__init__(**kwargs)
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}" # URL da pagina
        self.start() # Inicia a thread
        
    def run(self):
        time.sleep(20*random.random())
        r = requests.get(self._url)
        page_contents = html.fromstring(r.text)
        price = page_contents.xpath('//fin-streamer[@data-field="regularMarketPrice"]/text()')[0]
        print(price)