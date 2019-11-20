import datetime
import colorama
import trio
import asyncio

# this example is the same as "AsyncronousExample" but using TRIO library. Results the same.


async def generate_data(num, data):
    for i in range(1, num + 1):
        item = i * i
        await data.put((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + "-- generated item {}".format(i), flush=True)
        await trio.sleep(0.5)


async def process_data(num, data):
    processed = 0
    while processed < num:
        item = await data.get()
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
        await trio.sleep(0.5)


async def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App Started", flush=True)
    data = asyncio.Queue()

    async with trio.open_nursery() as nursery:  # nursery spams child processes
        nursery.start_soon(generate_data, 20, data, name="producer 1")
        nursery.start_soon(generate_data, 20, data, name="producer 2")
        nursery.start_soon(process_data, 20, data, name="consumer 1")

    dt = datetime.datetime.now() - t0
    print(
        colorama.Fore.WHITE,
        "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()),
    )


if __name__ == "__main__":
    trio.run(main)
