# Data Scraping (link collector)

This script will collect all links from a given URL, and if depth is greater than zero, it also collect the links of collected links and so on. So after they retrieve all links, it'll save the links and the datetime it was collected in a excel file (.xlsx).

## How to run?
1 - Clone the repository
```
git clone https://github.com/gph/link-collector.git
```

2 - Install dependencies
```
pip install bs4
pip install requests
pip install pandas
```
3 - How to import

```
from link_collector import LinkCollector

links_collected = LinkCollector('https://example.com/', 1)

# start collecting
links_collected.collect()

# print to console
links_collected.print()

# export to excel file
links_collected.export()

# get a list of links collected
links_list = links_collected.list

# get the dataframe
dataframe = links_collected.dataframe
```

4 - How to run on console
```
python .\link_collector.py https://example.com/ 0 
```
<i>WARNING: link_collector.py should receive two parameters URL and DEPTH in this order as the example above.</i>

4 - The spreadsheet will be created inside the app directory.
```
links-collected_TIMESTAMP.xlsx
```

<i>PS: I did it for a job interview assignment.</i>