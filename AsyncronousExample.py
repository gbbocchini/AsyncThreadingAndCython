import datetime
import asyncio
import colorama
import uvloop


async def generate_data(num, data):
    for i in range(1, num + 1):
        item = i * i
        await data.put((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + "-- generated item {}".format(i), flush=True)
        await asyncio.sleep(0.5)


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
        await asyncio.sleep(0.5)


def main():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())  # uvloop for boooost!
    loop = asyncio.get_event_loop()  # async events/functions loop

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App Started", flush=True)
    data = asyncio.Queue()  # async jobs Queue (first in/first out)

    task0 = loop.create_task(
        generate_data(20, data)
    )  # generator style: nothing is made until "run_until_complete"
    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(process_data(20, data))
    final_task = asyncio.gather(task0, task1, task2)  # necessary when more than 1 task

    loop.run_until_complete(final_task)  # runs the functions above asynchronously

    dt = datetime.datetime.now() - t0
    print(
        colorama.Fore.WHITE,
        "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()),
    )


if __name__ == "__main__":
    main()
