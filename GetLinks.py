import json

import bs4
import requests

plantname = input("请输入植物学名：")
mainpage = bs4.BeautifulSoup(requests.get(
    "http://www.plant.csdb.cn/photo?sname=&chname={}&creator=&province=&loc=&habit=&year=".format(plantname)).text,
                             'html.parser')
num = int(mainpage.find('font').get_text())
page = int(num / 50)
piclist = []
for p in range(0, page + 1):
    nowpage = bs4.BeautifulSoup(requests.get(
        'http://www.plant.csdb.cn/photo?page={}&sname=&chname={}&creator=&province=&loc=&habit=&year='.format(p,
                                                                                                              plantname)).text,
                                'html.parser')
    pics = nowpage.find_all('img', width='100')
    for pic in pics:
        a = pic.parent['href']
        picpage = bs4.BeautifulSoup(requests.get('http://www.plant.csdb.cn/' + a).text, 'html.parser')
        picreal = picpage.find('img')
        piclist.append(picreal['src'])
with open(plantname + '.json', 'w') as f:
    json.dump(piclist, f)
