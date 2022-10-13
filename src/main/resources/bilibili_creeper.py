import requests  # 向页面发送请求
from bs4 import BeautifulSoup  # 解析页面
import time
import csv
import json
url = 'https://app.bilibili.com/x/v2/search/trending/ranking?csrf=4b5803a88c3205d9f228328c05e02ced&limit=50'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.42',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',

}
r = requests.get(url, headers=header)


class TopRecord:
    title: ''
    ranking: 0
    popularity: ''


data = json.loads(r.text)
li = data['data']['list']
records = []
for data in li:
    record = TopRecord()
    record.ranking = data['position']
    record.title = data['show_name']
    record.popularity = 'Not Given'
    records.append(record)
import time
import csv

t = time.localtime()
time_str = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + " " + str(t.tm_hour) + ":" + str(t.tm_min)
with open("bilibili.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for record in records:
        writer.writerow([record.ranking, record.title, record.popularity, time_str, "bilibili"])
