import time

from workers.wikipedia_reader import WikiWorker
from workers.yahoo_finance_reader import YahooFinanceWorker

def main():
    calc_start_time = time.time()
    current_workers = []
    wikiworker = WikiWorker()
    for symbol in wikiworker.get_sp_500_companies():
        yahooFinancePriceWorker = YahooFinanceWorker(symbol=symbol)
        current_workers.append(yahooFinancePriceWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].start()

    for i in range(len(current_workers)):
        current_workers[i].join()

    print('Extracting time took:', round(time.time() - calc_start_time,1))