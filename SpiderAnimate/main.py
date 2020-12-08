# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -*- codeing =utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    baseurl = "https://konachan.net/post?page="
    # getData(baseurl)
    # 1.爬取网站
    datalist = getData(baseurl)
    # savepath="豆瓣电影Top250.xls"
    # saveData(datalist,savepath)

    dbpath = "animatePicDB.db"
    saveDataDB(datalist, dbpath)

    # askURL("https://konachan.net/post?page=1")


# herf的规则
findLink = re.compile(r'<a class="thumb" href="(.*?)">')
# Tags的规则
findTags = re.compile(r'Tags:(.*?)User:')
# imageScr规则
findImg = re.compile(r'src="(.*?)"')


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):  # 调用获取页面信息的函数10次
        url = baseurl + str(i + 1)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('a', class_="thumb"):  # 查找符号要求的字符串，返回列表
            # print(item) #测试，查看图片thumb的所有信息
            data = []  # 保存爬取图片的所有信息
            item = str(item)

            # 获取herf超链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            # print(link)

            # 获取ImgSrc
            ImgSrc = re.findall(findImg, item)
            ImgSrc = re.sub("\[", " ", ImgSrc[0])  # 去掉['']
            data.append(ImgSrc)
            # print(ImgSrc)

            # 获取Tag
            tags = re.findall(findTags, item)[0]
            data.append(tags)
            # print(tags)

            datalist.append(data)

    # print(datalist)
    return datalist


# 得到一个指定一个URL网页的内容(测试网页是否能爬虫
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }  # 用户代理：本质是告诉浏览器，我们能接受什么水平的文件内容

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 3.保存数据
# 创建数据库
def init_db(dbpath):
    sql = '''
    create table animatePic
    (
    id integer primary key autoincrement,
    pic_link text,
    info_link text,
    tags varchar
    )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
                insert into animatePic
                (
                info_link, pic_link, tags)
                values(%s)''' % ",".join(data)
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

    print("db")


if __name__ == '__main__':
    main()
    # init_db("movie.db")
    print_hi('PyCharm')
