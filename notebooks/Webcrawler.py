from bs4 import BeautifulSoup
import requests
import cssutils
import validators
import sys
import pandas as pd

def get_content(url):
    return requests.get(url).text

url_input = "https://www.welt.de/"
#url_input = input("enter a valid URL to scape from ")
if validators.url(url_input):
 
    content = get_content(url_input)
    soup = BeautifulSoup(content)
    tag_array = []
    for tag in soup.findAll():
        tag_array.append(tag.name)

else:
    print("invalid URL")
    sys.exit
print(tag_array[1])

    
