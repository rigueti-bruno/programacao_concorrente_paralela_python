import time

def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2
    print(sum_squares)
    
def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    for i in range(5):
        calculate_sum_squares(i)
    
    print(f"Calculate sum of squares took: {round((time.time() - calc_start_time),1)} seconds")
    
    sleep_start_time = time.time()
    for i in range(1,6):
        sleep_a_little(i)
    print(f"Sleep took: {round((time.time() - sleep_start_time),1)} seconds")
    
if __name__ == "__main__":
    main()