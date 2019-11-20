import datetime
import math_core
import multiprocessing
from threading import Thread

# compare the results of this X "compute_multiprocesses_AsyncPool.py". Amazing!


def main():
    math_core.do_math(1)

    t0 = datetime.datetime.now()

    print("Doing math on {:,} processors".format(multiprocessing.cpu_count()))

    processor_count = multiprocessing.cpu_count()
    threads = []
    for i in range(1, processor_count + 1):
        threads.append(
            Thread(
                target=math_core.do_math,
                args=(
                    30_000_000 * (i - 1) / processor_count,
                    30_000_000 * i / processor_count,
                ),
                daemon=True,
            )
        )

    [t.start() for t in threads]
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec".format(dt.total_seconds()))


if __name__ == "__main__":
    main()
