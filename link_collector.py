import re
import sys
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup


def _search_for_links(url) -> dict:
    """ it returns a dictionary of links {URL: "datetime it's collected"} """

    try:
        response = requests.request('GET', url)
    except Exception as e:
        print(f'{e}\nERROR: Probably wrong url... but it could be a connection problem!')
        return {}

    raw_content = response.content
    content = BeautifulSoup(raw_content, 'html.parser', from_encoding='iso-8859-1')

    links_found = {}

    for item in content.findAll('a', attrs={'href': re.compile("^http(s|)://")}):
        link = item.get('href')
        if link not in links_found.keys():
            links_found[link] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    return links_found


class LinkCollector:

    def __init__(self, url: str, depth: int = 0):
        self.links_list = {}
        self.url = url
        self.depth = depth

    def collect(self) -> None:
        links = _search_for_links(self.url)
        total_links_found = links.copy()

        if self.depth > 0:
            for _ in range(self.depth):
                temp_dict = {}

                for link in links:
                    temp_dict.update(_search_for_links(link))

                total_links_found.update(temp_dict)
                links = temp_dict  # links are set for the next iteration
        self.links_list = total_links_found.items()

    def __str__(self) -> str:
        result = ''
        for link in list(self.links_list):
            result += f'{link[1]} {link[0]}\n'
        return result

    def export_to_excel(self) -> None:
        filename = f'link-collector_{datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx'
        dataframe = pd.DataFrame(self.links_list, columns=['link', 'time'])
        dataframe.to_excel(filename, sheet_name="links", index=False)


def main():
    try:
        url = sys.argv[1]
        depth = int(sys.argv[2])
    except IndexError:
        print('Example: link_collector.py <URL> <DEPTH>')
        return

    zero_depth = LinkCollector(url, depth)

    # collect links
    zero_depth.collect()
    # output data to console
    print(zero_depth)
    # generate an excel file
    zero_depth.export_to_excel()


if __name__ == "__main__":
    main()
