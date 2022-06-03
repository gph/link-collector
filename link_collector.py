from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import pandas as pd
from datetime import datetime

def getLinks(URL, depth, fileName):
    links = getLinksFrom(URL)
    linksTotal = links.copy()

    if depth > 0:
        for _ in range(depth):
            tempDict = {}
            
            for link in links:
                tempDict.update(getLinksFrom(link))
                           
            linksTotal.update(tempDict)
            links = tempDict # links are set for the next iteration
    
    dataframe = pd.DataFrame(linksTotal.items(), columns = ['link', 'atualTime'])
    dataframe.to_excel(fileName, sheet_name="links", index=False)

def getDateTime():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S") # current date and time

def getLinksFrom(URL):
    try:
        response = requests.request('GET', URL)
    except:
        return {} # if URL not work

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    linksDict = {}

    for item in soup.findAll('a', attrs={'href': re.compile("^http(s|)://")}):
        link = item.get('href')
        linksDict[link] = getDateTime()

    return linksDict

# example
#getLinks("https://enttry.com.br/contato", 0, 'linksEnttry.xlsx')