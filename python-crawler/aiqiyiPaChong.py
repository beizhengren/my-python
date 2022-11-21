import zlib
import requests
from bs4 import BeautifulSoup
import requests
import time
import xlwt
import re#对解析后的文件进行弹幕匹配
import pandas as pd
import csv
import os
# tv_id_module = __import__('tv_id')


def get_bullet(tv_id):
    for page in range(1, 27):
        # https://cmts.iqiyi.com/bullet/tv_id[-4:-2]/tv_id[-2:]/tv_id_300_x.z
        url = 'https://cmts.iqiyi.com/bullet/' \
              + tv_id[-4:-2] + '/' \
              + tv_id[-2:] + '/' \
              + tv_id + '_300_' \
              + str(page) + '.z'
        print(url)

        # 请求弹幕压缩文件
        res = requests.get(url).content
        res_byte = bytearray(res)
        root = os.getcwd()
        try:
            xml = zlib.decompress(res_byte).decode('utf-8')
            format = re.compile("<content>(.*?)</content>")
            DanMu = format.findall(xml)
            print(DanMu)
            # 保存路径
            path = os.path.join(root, tv_id + '_300_' + str(page) + '.csv')

            with open(path, "w+", newline='',encoding='utf-8-sig') as csvFile:

                for i in DanMu:
                    print(i)
                    csvFile.write(i)
                    csvFile.write(",")
                    csvFile.write("\n")

        except:
            return


def main():
    my_tv_id_list = [15303652400, 15237421000, 15235939800, 15068748500, 15068699100, 14992525500, 14992485500,
                     14812230700, 14812202100, 14722978600, 14722962600, 14520454600, 14520762300, 14426429300,
                     14425793300, 14224268700, 14219902900, 14139369700, 14140651000, 13958052300, 13950421000,
                     13847100500, 13661233000]
    for i in my_tv_id_list:
        get_bullet(str(i))
        f.save('Movies.xls')#这里应该是多余的，空的

if __name__ == '__main__':
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet('Movies')#多余
    main()
