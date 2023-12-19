import bs4 as BeautifulSoup
import requests
import cssutils
import validators
import sys
import pandas as pd

def get_content(url):
    return requests.get(url).text

url_input = input("enter a valid URL to scape from ")
if validators.url(url_input):
    webseite = get_content(url_input)
    results = BeautifulSoup(webseite.get_content, 'html.parser')
    print(results)
else:
    print("invalid URL")
    sys.exit
    


    
    
