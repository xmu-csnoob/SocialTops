import requests  # 向页面发送请求
from bs4 import BeautifulSoup  # 解析页面
import time
import csv
url = 'https://www.zhihu.com/billboard'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 Edg/106.0.1370.42',
    'Host': 'www.zhihu.com',
    'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accept-Encoding': 'gzip, deflate',
    # 定期更换Cookie
    'Cookie': '_zap=0af2ebf2-39ae-4d8d-bd87-9c35f11bff03; d_c0="AAAQyP65BhWPTmgOm0VsK23y9NsMYO1zPNU=|1654008663"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=oQZjYYZpVeZBRFERFAbBElfZ%2Fe%2B%2B4vwE; YD00517437729195%3AWM_NI=urgT6suKBZ%2FsjSYqf7egJNyNKqD5ooelUWbZnT5fq%2BVV9Kve1%2BuKLm16sg2Xe8Ar2pRLgfPkkP3oTiZLI7FcaU2eVJauOUhkBL%2FO5HC%2FK4D%2Fi7Q780DXCVK45GoeDP3AcEY%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee86ec68ab978baeea5db78e8ba6c85a978f8a82c449f699e1b2ea7097eaa5b7d22af0fea7c3b92ab7aea9b5b579b7958ebbae79aa8d9792e53da7b986affc4689af8cd6ee65a7b49bb8e152ae8cfb87f421968af7acf56ff3f5bbaccf67f3eabd88b154a7e88f93b17c9294a987d361a990fd90d7639a9487d8c569a38bfe86d542a3ab81b6eb618294e1b0b84481f185d5c725abe99fd8bb3c88888db7ca40f799a186c75cf19fada6dc37e2a3; gdxidpyhxdE=Bt1bJ9x2X0qMR%2Fx2LnPHoDwxGYV2%2B503LLisol3vKziNEyK8u%2BuARQrEUbaU%5CYaPCOoGurIf%5C033L%5Cn3xnHLY%2B3vqURZP5mUYfP1uckNiRwMi8TZps5ktCDZKUslk9tru%2B%5CCxlJmglGC9iV5B5Aw7Vsjk2OGie8tygkE0idnUv%2BmIvTL%3A1665628082097; ariaDefaultTheme=undefined; captcha_session_v2=2|1:0|10:1665672740|18:captcha_session_v2|88:TThNdTFUeG9nK2tDQ2ErTWRiYURnTTdWZUVDOFkyOVQyVVRjaVBxb1NCMUhXZ1F0UDJnRGxLRzJQc3NhQ3kxbA==|1e71966d74604cdab845d15ca2acf2338650df7bf145891cd984e89dd9dc1b40; _xsrf=323aac82-f8a4-481d-a192-d6b056118395; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1665626339,1665634923,1665652269,1665709999; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1665709999; SESSIONID=2dH3I6vbmcKWooKjJOxMqehp5RXzkMRgKQdRkckE1P9; JOID=VlkQBkw8JdUgkzg6LTyjStuRgzo5C0WdEdkLSE9SQ5p3_lR0Q5KWn0KVOT4vnzRxIjr3XWqv4TvC_fgUUY1H8q8=; osd=V14QC0I9ItUtnTk9LTGtS9yRjjQ4DEWQH9gMSEJcQp1381p1RJKbkUOSOTMhnjNxLzT2Wmqi7zrF_fUaUIpH_6E=; KLBRSID=fe78dd346df712f9c4f126150949b853|1665710000|1665709997'
}
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find('div', {'class': 'Card'})
records = []


class TopRecord:
    ranking: ''
    title: ''
    popularity: ''


for item in items:
    # print(item)
    record = TopRecord()
    ranking = item.find('div', {'class': 'HotList-itemIndex HotList-itemIndexHot'})
    if ranking is not None:
        record.ranking = ranking.text
        title = item.find('div', {'class': 'HotList-itemTitle'})
        record.title = title.text
        popularity = item.find('div', {'class': 'HotList-itemMetrics'})
        popularity = popularity.text
        strs = str.split(popularity, " ")
        record.popularity = strs[0]
        records.append(record)
    else:
        ranking = item.find('div', {'class': 'HotList-itemIndex'})
        if ranking is not None:
            record.ranking = ranking.text
            title = item.find('div', {'class': 'HotList-itemTitle'})
            record.title = title.text
            popularity = item.find('div', {'class': 'HotList-itemMetrics'})
            popularity = popularity.text
            strs = str.split(popularity, " ")
            record.popularity = strs[0]
            records.append(record)
        else:
            continue

t = time.localtime()
time_str = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + " " + str(t.tm_hour) + ":" + str(t.tm_min)

with open("zhihu.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for record in records:
        writer.writerow([record.ranking, record.title, record.popularity, time_str, "知乎"])
