import time

from multiprocessing import Queue

from workers.wikipedia_reader import WikiWorker
from workers.yahoo_finance_scheduler import YahooFinancePriceScheduler
from workers.PostgresWorker import PostgresMasterScheduler


def main():
    symbol_queue = Queue()
    postgres_queue = Queue()
    calc_start_time = time.time()
    
    wikiWorker = WikiWorker()
    yahoo_finance_scheduler_threads = []
    num_yahoo_finance_price_workers = 4
    for i in range(num_yahoo_finance_price_workers):
        yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue, output_queue=postgres_queue)
        yahoo_finance_scheduler_threads.append(yahooFinancePriceScheduler)

    postgres_scheduler_threads = []
    num_postgres_workers = 2
    for i in range(num_postgres_workers):
        postgresScheduler = PostgresMasterScheduler(input_queue=postgres_queue)
        postgres_scheduler_threads.append(postgresScheduler)
    
    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)
        
    for i in range(len(yahoo_finance_scheduler_threads)):
        symbol_queue.put('DONE')
        
    for i in range(len(yahoo_finance_scheduler_threads)):
        yahoo_finance_scheduler_threads[i].join()
        


    print('Extracting time took:', round(time.time() - calc_start_time,1))
    
if __name__ == "__main__":
    main()