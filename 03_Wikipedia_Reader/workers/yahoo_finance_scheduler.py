import threading
import requests
import time
from bs4 import BeautifulSoup
from lxml import html
import random

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self,input_queue,**kwargs):
        super(YahooFinancePriceScheduler,self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start() # Inicia a thread
    
    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break
            yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=val)
            price = yahooFinancePriceWorker.get_price()
            print(price)


class YahooFinancePriceWorker():
    def __init__(self, symbol, **kwargs):        
        self._symbol = symbol
        base_url = "https://finance.yahoo.com/quote/"
        self._url = f"{base_url}{self._symbol}" # URL da pagina
        
        
    def get_price(self):        
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        r = requests.get(self._url, headers=headers)
        if r.status_code != 200:            
            return ""
        page_contents = html.fromstring(r.text)
        price = float(page_contents.xpath('//*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span')[0].text)
        return price