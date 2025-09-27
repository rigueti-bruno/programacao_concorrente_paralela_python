import time
import threading

def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)
    
def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    
    current_thread = []
    for i in range(5):
        max_value = (i+1)*1000000
        t = threading.Thread(target=calculate_sum_squares, args=(max_value,))
        t.start()
        current_thread.append(t)
    
    for i in range(len(current_thread)):
        current_thread[i].join()
    
    print(f"Calculate sum of squares took: {round((time.time() - calc_start_time),1)} seconds")
    
    sleep_start_time = time.time()
    current_sleep_thread = []
    for i in range(1,6):
        max_value = i
        t = threading.Thread(target=sleep_a_little, args=(max_value,)) # instancia a thread
        # target=sleep_a_little: atribui a função à thread
        t.start() # inicia a execução da thread
        current_sleep_thread.append(t)
    for i in range(len(current_sleep_thread)):
        current_sleep_thread[i].join()
    print(f"Sleep took: {round((time.time() - sleep_start_time),1)} seconds")
    
if __name__ == "__main__":
    main()