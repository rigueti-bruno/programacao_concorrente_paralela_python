import time

from multiprocessing import Queue

from workers.wikipedia_reader import WikiWorker
from workers.yahoo_finance_scheduler import YahooFinancePriceScheduler


def main():
    symbol_queue = Queue()
    calc_start_time = time.time()
    
    wikiWorker = WikiWorker()
    yahoo_finance_scheduler_threads = []
    yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
    yahoo_finance_scheduler_threads.append(yahooFinancePriceScheduler)
    
    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)
        
    for i in range(len(yahoo_finance_scheduler_threads)):
        symbol_queue.put('DONE')
        
    for i in range(len(yahoo_finance_scheduler_threads)):
        yahoo_finance_scheduler_threads[i].join()
        """
        yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=symbol)
        current_workers.append(yahooFinancePriceWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
        """


    print('Extracting time took:', round(time.time() - calc_start_time,1))
    
if __name__ == "__main__":
    main()