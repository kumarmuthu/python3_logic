__version__ = "2024.07.20.01"
__author__ = "Muthukumar Subramanian"

"""
Thread Execution
"""

import threading
import time
import multiprocessing


def worker(delay, name):
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} finished")


def run_with_join():
    print("{:#^30}".format("Start - run_with_join"))
    # Create two threads
    thread1 = threading.Thread(target=worker, args=(2, 'A'))
    thread2 = threading.Thread(target=worker, args=(3, 'B'))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print("Both threads have finished")
    print("{:#^30}".format("End - run_with_join"))


def run_without_join():
    print("{:#^30}".format("Start - run_without_join"))
    # Create two threads
    thread1 = threading.Thread(target=worker, args=(5, 'C'))
    thread2 = threading.Thread(target=worker, args=(10, 'D'))

    # Start the threads
    thread1.start()
    thread2.start()

    print("Both threads have finished")
    print("{:#^30}".format("End - run_without_join"))


def main_script():
    run_with_join()
    run_without_join()


if __name__ == '__main__':
    print("{:#^30}".format("Script Start"))
    multiprocess_obj = multiprocessing.Process(target=main_script)
    multiprocess_obj.start()
    multiprocess_obj.join(timeout=30)
    if multiprocess_obj.is_alive():
        multiprocess_obj.terminate()

    print("{:#^30}".format("Script End"))
