""" parkrun_scraper.py that scrapes pr website table data and saves as csv"""

# for timestamping
import time

# for accessing url
from io import StringIO

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present on the website
from html_table_parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

# for accessing url
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
}
url = "https://www.parkrun.ie/parkrunner/472100/all/"
# Array of column headers expected
table_titles = ["Summary Stats for All Locations", "Best Overall Annual Achievements",
        "All Results"]

## LIVE DATA ##
# https request and obtaining StringIO object and convert to html and print
output = StringIO(requests.get(url, headers=headers).text)
html_extract = output.read()
timestr = time.strftime("%Y%m%d-%H%M")
file_path = f"parkrun-scrape-results_{timestr}.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_extract)


## STATIC DATA ##
# Specify the path to your local HTML file
""" file_path = "C:/Users/daire/wa/parkrun-app/
view-source_https___www.parkrun.ie_parkrunner_472100_all_STATIC_HTML.html"""

# Open the file in read mode
with open(file_path, mode="r", encoding="utf-8") as file:
    # Read the contents of the file
    html_data = file.read()

# Parser
p = HTMLTableParser()
p.feed(html_data)

for table_index, table_data in enumerate(p.tables):
    print("\n")
    print(table_titles[table_index])
    print("\nTABLE: \n")
    pprint(table_data)

    # Converting the parsed data to a dataframe
    print("\nPANDAS DATAFRAME\n")
    print(table_titles[table_index])
    print(pd.DataFrame(table_data))

## Write to csvs and pass to BI/kotlin/android app for visualisation/further manipulation.
df=pd.DataFrame(p.tables[2])
df[4] = '`' + df[4].astype(str)


df.to_csv('out.csv',date_format=None,index=False,mode='w')
