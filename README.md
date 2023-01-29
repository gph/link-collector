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
pip install -r requirements.txt
```

3 - How to import

```
url = 'https://example.com/'

list_links_found = search(url=url, depth=1).items()
    
sorted_by_datetime = sorted(list_links_found, key=lambda d: d[1])

for link, dt in sorted_by_datetime:
    print(f'{dt} {link}')
```
<i>PS: I did it for a job interview assignment.</i>
