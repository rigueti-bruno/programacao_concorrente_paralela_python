# Função Principal do Programa:

import time
from classes.SleepyWorkers import SleepyWorker
from classes.SquareSumWorkers import SquareSumWorker

def main():
    calc_start_time = time.time()
    
    # executa os threads com a função de soma dos quadrados:
    current_workers = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        squaredSumWorker = SquareSumWorker(maximum_value)
        current_workers.append(squaredSumWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()  # espera o término do thread
        
    print('Calculating sum of squares took: ', round(time.time() - calc_start_time, 1))
    
    # executa os threads com a função de sleep:
    sleep_start_time = time.time()
    current_workers = []
    for seconds in range(1,6):
        sleepWorker = SleepyWorker(seconds=seconds)
        current_workers.append(sleepWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()  # espera o término do thread
        
    print('Sleep took: ', round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()