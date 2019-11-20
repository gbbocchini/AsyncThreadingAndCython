import datetime
import colorama
import time
import random
import threading


def generate_data(num, data):
    for i in range(1, num + 1):
        item = i * i
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + "-- generated item {}".format(i), flush=True)
        time.sleep(random.random() + 0.5)


def process_data(num, data):
    processed = 0
    while processed < num:
        item = None
        if data:
            item = data.pop(0)
        if not item:
            time.sleep(0.01)
            continue
        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t
        print(
            colorama.Fore.CYAN
            + "++ Processed value {} after {:,.2f} sec".format(
                value, dt.total_seconds()
            )
        )
        time.sleep(0.5)


def main():
    t0 = datetime.datetime.now()

    data = []

    threads = [
        threading.Thread(target=generate_data, args=(20, data), daemon=True),
        threading.Thread(target=process_data, args=(20, data), daemon=True),
    ]

    print("Starting...")

    [i.start() for i in threads]
    [i.join() for i in threads]

    dt = datetime.datetime.now() - t0
    print(
        colorama.Fore.WHITE
        + "App exiting, total time: {} sec".format(dt.total_seconds())
    )


if __name__ == "__main__":
    main()
