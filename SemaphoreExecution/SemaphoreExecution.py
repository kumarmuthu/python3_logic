__version__ = "2024.07.20.01"
__author__ = "Muthukumar Subramanian"

"""
Semaphore Execution
"""

import threading
import time
import multiprocessing

# Define a semaphore with an initial value of 5
semaphore = threading.Semaphore(5)


def worker(each_id):
    with semaphore:
        print(f"Worker {each_id} acquired the semaphore")
        time.sleep(2)
        print(f"Worker {each_id} released the semaphore")
        time.sleep(2)


def main_script():
    # Create 10 worker threads
    threads = []

    for i in range(10):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All workers have completed")


if __name__ == '__main__':
    print("{:#^30}".format("Script Start"))
    multiprocess_obj = multiprocessing.Process(target=main_script)
    multiprocess_obj.start()
    multiprocess_obj.join(timeout=15)
    if multiprocess_obj.is_alive():
        multiprocess_obj.terminate()

    print("{:#^30}".format("Script End"))
