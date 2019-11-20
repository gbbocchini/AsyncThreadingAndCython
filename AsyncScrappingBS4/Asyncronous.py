import bs4
from colorama import Fore
import datetime
import aiohttp  # runs only in a context-manager with asyncio (async_with // async WITH implementation)
import asyncio
import uvloop


async def get_html(episode_number):
    print(
        Fore.YELLOW + "Getting HTML for episode {}".format(episode_number), flush=True
    )

    url = "https://talkpython.com/{}".format(episode_number)

    async with aiohttp.ClientSession() as client:  # open an aiohttp client session
        async with client.get(
            url
        ) as response:  # the client gets the url async (awaits for the response)
            response.raise_for_status()
            return (
                await response.text()
            )  # the func awaits untill the contents of response being saved/loaded in memory


def get_title(html, episode_number):
    print(
        Fore.CYAN + "Getting the TITLE for episode {}".format(episode_number),
        flush=True,
    )
    soup = bs4.BeautifulSoup(html, "html.parser")
    header = soup.select_one("h1")
    if not header:
        return "Missing"

    return header.text.strip()


async def get_title_range():
    tasks = []
    for i in range(115, 125):
        tasks.append(
            (i, asyncio.create_task(get_html(i)))
        )  # fist start all tasks (generators)

    for n, t in tasks:  # then we process them all!
        html = await t
        title = get_title(html, n)
        print(Fore.WHITE + "Title found: {}".format(title), flush=True)


def main():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    t0 = datetime.datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())  # only 1 task
    t1 = datetime.datetime.now()
    tfinal = t1 - t0
    print("Done in {}.".format(tfinal.total_seconds()))


if __name__ == "__main__":
    main()
