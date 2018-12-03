#Reference: http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
#Reference: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

from nytimesarticle import articleAPI
import csv 
#from bs4 import BeautifulSoup
#import re
import requests
# import urllib.requests
from bs4 import BeautifulSoup
import time
import sys

api = articleAPI('ade20c096c624ac3bcde8664e228e8fa')
start_index=10
end_index=100
j=start_index
topics=['Sports']
reload(sys)
sys.setdefaultencoding('utf-8')

for search_word in topics :
    j=start_index
    while j < end_index:
        articles = api.search( q = search_word, offset = j)
        url_count = 0
        for i in articles['response']['docs']:
            filename=search_word+str(j)+str(url_count)+'.txt'
            nytimesData = open(filename, 'a+')
        
            url = i['web_url']
            r = requests.get(url)
            time.sleep(5)
            soup = BeautifulSoup(r.content, 'html.parser')
            for script in soup.find_all('script'):
                script.extract()
            pTags = soup.findAll("p", text=True)
            for paragraph in pTags:
                para=paragraph.get_text(strip=True)
                print(para)
                nytimesData.write(para)
            nytimesData.close()
            url_count += 1
        j += 1