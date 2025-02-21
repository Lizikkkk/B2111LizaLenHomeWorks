import time
import logging

logging.basicConfig(level=logging.INFO)

def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    logging.info(f"Функція виконалася за {time.time() - start:.6f} секунд")
    return result

def sample_function(n):
    time.sleep(n)
    return n * 2

measure_time(sample_function, int(input("Скільки секунд буде тривати функція? ")))