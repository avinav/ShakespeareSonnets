'''
Created on Apr 27, 2015

@author: avinav
'''
import ConfigParser
import numpy as np
import requests
from bs4 import BeautifulSoup
from Parser import Parse

def crawl(url, **kwargs):
    doc_path = kwargs.get('doc_path')
    atags = getChildren(url)
    i = 0
    for atag in atags:
        if ( i == 1):
            break
        name = atag.content
        nexturl = url + atag['href']
        r = requests.get(nexturl)
        soup = BeautifulSoup(r.text)
        content = soup.find_all('tr')[1].td
        # Remove br from content
        for e in content.find_all('br'):
            e.extract()
        doc = Parse.parse(atag['href'], content.text, doc_path)
        i += 1
    
def getChildren(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    trows = soup.find_all('tr')
    atags = trows[1].find_all('a')
    return atags
    
#---- Script starts here
Config = ConfigParser.ConfigParser()
Config.read("../util/indexer.cfg")
url = Config.get("crawler","url")
doc_path = Config.get("parser","doc_path")
crawl(url, doc_path=doc_path)

    
