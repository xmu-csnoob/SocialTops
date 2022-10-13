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
    'Cookie': 'SINAGLOBAL=1812089928092.4663.1665389189803; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWvBg5bKW0M6oiD6r2Uu1pP5JpX5KMhUgL.FozpSK.71heRSKe2dJLoI74SwHSaUgpz9PiF9g8XM7tt; ALF=1697188065; SSOLoginState=1665652067; SCF=AmoZWOX-xUmDMUIpuTQ6gpL1yMBYb0JbAOSF28HIGIIWg34Ps369M02JYMYDRkDw7UekpU4eCB5NVQc_J7YKJxk.; SUB=_2A25OQ6UzDeRhGeRP7lsR-C3Ezj-IHXVtOJH7rDV8PUNbmtAfLWzAkW9NUA2CM5oYXNXK9-eAgopxHsEbq5BxszHj; _s_tentry=login.sina.com.cn; Apache=366329942574.95667.1665652068651; ULV=1665652068671:3:3:3:366329942574.95667.1665652068651:1665479629575; UOR=,,cn.bing.com'
}
r = requests.get(url, headers=header)
print(r.text)
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
