# encoding:UTF-8

from bs4 import BeautifulSoup
import re
import time
import urllib.request

price = ""
while True:
    time.sleep(30)
    url = "https://www.tking.cn/content/58a6baa40cf29be0660beddc"
    data = urllib.request.urlopen(url).read()
    html = data.decode('UTF-8')
    # minPrice =
    # print(data)

    bsObj = BeautifulSoup(html, "lxml")  # 将html对象转化为BeautifulSoup对象
    ulList = bsObj.findAll("script")  # 找到所有ul
    ul = str(ulList[5])

    print(price)
    # minPrice = re.sub("\D", "", ul)
    # minPrice = re.sub(r"currentShowMinPrice = '(\D)'","", ul)
    minPrice = re.search("currentShowMinPrice = '(\d+)'", ul).group(1)
    if price!=minPrice:
        print("当前最低票价:" + minPrice + "元")
        price=minPrice
        url = "https://sc.ftqq.com/SCU4785Tcf49bc21ae679201b91320e990cf4bbf58639ffc513c3.send?text="+price
        response = urllib.request.urlopen(url)
