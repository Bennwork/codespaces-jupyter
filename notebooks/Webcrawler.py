#import beautifulsoup4
import requests
import cssutils
import validators
import sys

def get_content(url):
    return requests.get(url).text

url_input = input("enter a valid URL to scape from ")
if validators.url(url_input):
    content = get_content(url_input)
    print(content)
else:
    print("invalid URL")
    sys.exit
    


    
    
