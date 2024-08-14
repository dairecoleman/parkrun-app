# parkrun_scraper.py
# Library for opening url and creating 
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present 
# on the website
#from html_table_parser.parser import HTMLTableParser
from html_table_parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd
import csv

# for accessing url
from io import StringIO
import requests
print("itsworking")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
}
url = "https://www.parkrun.ie/parkrunner/472100/all/"

##  USE STATIC DATA FOR TESTING. MAYBE LOOK INTO CACHING THESE RESULTS ##

# https request and obtaining StringIO object and convert to html and print
# f = StringIO(requests.get(url, headers=headers).text)
# html_data = f.read()

## STATIC DATA ##
# Specify the path to your local HTML file
file_path = "C:/Users/daire/wa/Parkrun Project/view-source_https___www.parkrun.ie_parkrunner_472100_all_STATIC_HTML.html"
table_titles = ["Summary Stats for All Locations", "Best Overall Annual Achievements", "All Results"]

# Open the file in read mode
with open(file_path, "r") as file:
    # Read the contents of the file
    html_data = file.read()

#print(html_data)

# Parser
p = HTMLTableParser()
p.feed(html_data)
#pprint(p.tables[0])

for table in range(len(p.tables)):
    print("\n")
    print(table_titles[table])
    print("\nTABLE: \n")
    pprint(p.tables[table])

    # converting the parsed data to
    # dataframe
    print("\nPANDAS DATAFRAME\n")
    print(table_titles[table])
    print(pd.DataFrame(p.tables[table]))

## Clean PB? column 

## Write to csvs and pass to BI/kotlin/android app for visualisation/further manipulation.
df=pd.DataFrame(p.tables[2])
df[4] = '`' + df[4].astype(str)





df.to_csv('out.csv',date_format=None,index=False,mode='w')
#df.to_excel("out.xlsx")
## test http retrival was succesful, test data is goodi.e can we make tables from it are they good tables??