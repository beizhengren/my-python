# // An highlighted block
from bs4 import BeautifulSoup#负责解析网页源码
import requests#负责爬取网页源码
import re#对解析后的文件进行弹幕匹配
import csv
import xlwt
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
response = requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid=253182017", headers=headers)
html_doc = response.content.decode('utf-8')
format = re.compile("<d.*?>(.*?)</d>")
DanMu = format.findall(html_doc)
#逐个输出弹幕
for i in DanMu:
   print(i)

def main():
    root = os.getcwd()
    for i in DanMu:
      with open(os.path.join(root, "bilibili.csv"),"a", newline='',encoding='utf-8-sig') as csvfile:
        writer= csv.writer(csvfile)
        danmu = []
        danmu.append(i)
        writer.writerow(danmu)



if __name__ == '__main__':
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet('Movies')#多余
    main()
