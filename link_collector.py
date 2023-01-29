import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

""" simple script to retrieve links """


def _beautiful_filter(raw_content: str) -> dict:
    """ Return a dict of links found from html content """
    content = BeautifulSoup(raw_content, 'html.parser', from_encoding='iso-8859-1')

    links_found = {}

    for item in content.findAll('a', attrs={'href': re.compile("^http(s|)://")}):
        link = item.get('href')
        if link not in links_found.keys():
            links_found[link] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    return links_found


def search(url: {}, depth: int = 0) -> dict:
    """ Return a dict of links found """
    current_links = {}

    if type(url) is not dict:
        url = {url: datetime.now().strftime("%Y/%m/%d %H:%M:%S")}

    for link in url.keys():
        try:
            r = requests.get(link)
        except Exception as e:
            print(f'ERROR: probably an invalid url {e}')
            continue

        links_found = _beautiful_filter(r.content)

        for key, value in links_found.items():
            # setdefault will only update new values
            current_links.setdefault(key, value)

    # pass links collected before to a recursive_search
    if depth > 0:
        depth = depth - 1
        result = search(url=current_links, depth=depth)
        if result:
            for key, value in result.items():
                current_links.setdefault(key, value)

    return current_links


def main():
    url = 'https://example.com/'

    list_links_found = search(url=url, depth=2).items()

    sorted_by_datetime = sorted(list_links_found, key=lambda d: d[1])

    for link, dt in sorted_by_datetime:
        print(f'{dt} {link}')


if __name__ == "__main__":
    main()
