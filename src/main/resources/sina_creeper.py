import requests  # 向页面发送请求
from bs4 import BeautifulSoup  # 解析页面
import csv
import time

url = 'https://s.weibo.com/top/summary?cate=realtimehot'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    # 定期更换Cookie
    'Cookie': 'SINAGLOBAL=1812089928092.4663.1665389189803; SCF=AmoZWOX-xUmDMUIpuTQ6gpL1yMBYb0JbAOSF28HIGIIWg34Ps369M02JYMYDRkDw7UekpU4eCB5NVQc_J7YKJxk.; UOR=,,cn.bing.com; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWvBg5bKW0M6oiD6r2Uu1pP5JpVF02feoe4e05fehq4; SUB=_2AkMUFKrbdcPxrAFQnfEVxGjqaY5H-jynwcMtAn7uJhMyAxhu7gohqSVutBF-XKzCOLl9hHDjZgiL7M8zZRzCDdsr; _s_tentry=cn.bing.com; Apache=3116256655200.6377.1665709958821; ULV=1665709958839:4:4:4:3116256655200.6377.1665709958821:1665652068671'
}
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find('section', {'class': 'list'})


class TopRecord:
    title: ''
    ranking: 0
    popularity: ''


records = []
last_popularity = '0'
for li in items.findAll('li'):
    if li.find('strong') is not None:
        record = TopRecord()
        span = li.find('span')
        em = span.find('em')
        if len(em.text) != 0:
            record.popularity = em.text
            last_popularity = record.popularity
        else:
            record.popularity = last_popularity
        em.extract()
        ranking = li.find('strong')
        if ranking.text != '•':
            record.ranking = ranking.text
            record.title = span.text
            records.append(record)

t = time.localtime()
time_str = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + " " + str(t.tm_hour) + ":" + str(t.tm_min)
with open("sina.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for record in records:
        writer.writerow([record.ranking, record.title, record.popularity, time_str, "新浪微博"])
