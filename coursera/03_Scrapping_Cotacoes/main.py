import time

from workers.wikipedia_reader import WikiWorker
from workers.yahoo_finance_reader import YahooFinancePriceWorker

def main():
    calc_start_time = time.time()
    
    wikiWorker = WikiWorker()
    current_workers = []
    try:
        for symbol in wikiWorker.get_sp_500_companies():
            yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=symbol)
            current_workers.append(yahooFinancePriceWorker)
        
        for i in range(len(current_workers)):
            current_workers[i].join()

        print('Extracting time took:', round(time.time() - calc_start_time,1))
    except requests.exceptions.ContentDecodingError:
        print("")
        pass
    
if __name__ == "__main__":
    main()