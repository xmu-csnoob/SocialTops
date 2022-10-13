import requests  # 向页面发送请求
from bs4 import BeautifulSoup  # 解析页面
import time
import csv
import json
url = 'https://top.baidu.com/board?tab=realtime'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.42',
    'Host': 'top.baidu.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    # 定期更换Cookie
}
r = requests.get(url, headers=header)


soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find('div', {'class': 'SN-WEB-waterfall-item _1RC_Iyy7DpADG7Av5-QIBS'})


class TopRecord:
    title: ''
    ranking: 0
    popularity: ''


records = []
for item in items:
    spans = item.find_all_next('span')
    record = TopRecord()
    count = 0
    record_count = 0
    for span in spans:
        _class = span.get('class')
        if _class[0][0] == '-':
            count += 1
            continue
        style = span.get('style')
        if style is not None:
            record.ranking = span.text.strip()
            count += 1
            record_count += 1
        else:
            record.title = span.text.strip()
            count += 1
            record.popularity = "0"
        if count == 3:
            records.append(record)
            record = TopRecord()
            count = 0
    if record_count == 30:
        break


t = time.localtime()
time_str = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + " " + str(t.tm_hour) + ":" + str(t.tm_min)
with open("baidu.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for record in records:
        writer.writerow([record.ranking, record.title, record.popularity, time_str, "baidu"])
