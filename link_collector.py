import re
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import pandas as pd

class LinkCollector:

    def __init__(self, URL, DEPTH = 0):
        self.URL = URL
        self.DEPTH = DEPTH

    def __scrapper(self, URL):
        try:
            response = requests.request('GET', URL)
        except:
            return {}  # if URL not work

        content = response.content
        soup = BeautifulSoup(content, 'html.parser', from_encoding='iso-8859-1')

        links_found = {}

        for item in soup.findAll('a', attrs={'href': re.compile("^http(s|)://")}):
            link = item.get('href')
            links_found[link] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        return links_found
    
    def collect(self):
        links = self.__scrapper(self.URL)
        total_links_found = links.copy()
        
        if self.DEPTH > 0:
            for _ in range(self.DEPTH):
                temp_dict = {}

                for link in links:
                    temp_dict.update(self.__scrapper(link))

                total_links_found.update(temp_dict)
                links = temp_dict  # links are set for the next iteration
        self.list = total_links_found.items()
        self.dataframe = pd.DataFrame(self.list, columns=['link', 'time'])
    
    def print(self):
        print(self.dataframe.to_string(columns=None, header=True, index=True, formatters=None, index_names=True, max_rows=None, max_cols=None, show_dimensions=False, line_width=None))
    
    # export data to excel file
    def export(self):
        self.dataframe.to_excel(f'link-collector_{datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx', sheet_name="links", index=False)


if __name__ == "__main__":
    URL = sys.argv[1]
    DEPTH = int(sys.argv[2])
    
    zeroDepth = LinkCollector(URL, DEPTH)
    
    # collect links
    zeroDepth.collect()
    # output data to console
    zeroDepth.print()
    # generate an excel file
    zeroDepth.export()