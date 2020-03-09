import datetime
import os
import json

if (os.path.exists('crawling.json')):
    os.remove('crawling.json')
os.system('scrapy crawl crawling -o crawling.json')
articles = []

file = open('crawling.json', 'r')
objs = list(json.load(file))

for each in objs:
    if len(each['author']) != 0:
        each['date'] = datetime.datetime.strptime(each['date'], '%b %d, %Y')
        articles.append(each)

articles.sort(key=lambda elem: elem['date'], reverse=True)

articles = articles[0:5]
for each in articles:
    print(each)
