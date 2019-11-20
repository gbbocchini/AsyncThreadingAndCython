import requests
import bs4
from colorama import Fore
import datetime


def get_html(episode_number):
    print(
        Fore.YELLOW + "Getting HTML for episode {}".format(episode_number), flush=True
    )

    url = "https://talkpython.com/{}".format(episode_number)
    resp = requests.get(url)
    resp.raise_for_status()

    return resp.text


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


def get_title_range():
    for i in range(150, 160):
        html = get_html(i)
        title = get_title(html, i)
        print(Fore.WHITE + "Title found: {}".format(title), flush=True)


def main():
    t0 = datetime.datetime.now()
    get_title_range()
    t1 = datetime.datetime.now()
    tfinal = t1 - t0
    print("Done in {}.".format(tfinal.total_seconds()))


if __name__ == "__main__":
    main()
