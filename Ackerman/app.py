import ackerman
import sys
import threading
import numpy as np
import datetime
import cython
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor as PoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor
import multiprocessing

threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20)


def main():
    work = []
    for i in range(0,5):
        with PoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            t0 = datetime.datetime.now()
            m: cython.int = np.random.randint(0, 6)
            n: cython.int = np.random.randint(0, 6)
            f = executor.submit(ackerman.ack, m, n)
            work.append(f)
            t1 = datetime.datetime.now()
            final_time = t1-t0

        print("Ackerman of {} and {} is: {} in {:,.5f}".format(m,n,f.result(), final_time.total_seconds()))


if __name__ == '__main__':
    main()

