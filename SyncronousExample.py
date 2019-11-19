import datetime
import asyncio
import colorama
import time
import random


def generate_data(num, data):
    for i in range(1, num+1):
        item = i*i
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + "-- generated item {}".format(i), flush=True)
        time.sleep(random.random() + 0.5)


def process_data(num, data):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(0.01)
            continue
        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now()-t
        print(colorama.Fore.CYAN + "++ Processed value {} after {:,.2f} sec".format(value, dt.total_seconds()))
        time.sleep(0.5)


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App Started", flush=True)
    data = []

    generate_data(15, data)
    process_data(15, data)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {} sec".format(dt.total_seconds()))



if __name__ == "__main__":
    main()