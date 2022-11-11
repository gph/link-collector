# Data Scraping (link collector)

## How it works?
Should set two parameters: URL and DEPTH.

Depth means how much further you want to go.
If set to 0, it'll collect all hyperlinks from the given URL.
If set to 1, it'll do the same for every hyperlink found before.
and so on...

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
