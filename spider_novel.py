from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.wmtxt.com/23/23174/11594685.html';
browser = webdriver.Chrome();
#   打开chrome浏览器
browser.get(url);
#   打开url

i = 1;
while i<10 :
    html = BeautifulSoup(browser.page_source, 'html.parser');
    #   获取网页全部html信息
    link = html.find('p' , {'id' : 'articlecontent'}).get_text();
    #   查找标签为p,id为articlecontent的语句 , 并直接转化位文本形式
    #print(link);
    #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    time.sleep(1);
    #   程序暂停1s , 防止服务器不能及时响应
    with open('盗墓笔记.txt' , 'a' , encoding='utf-8' ) as f:
        f.write(link)
    #   with open 进行文件读写操作  文件名 ，‘a’ 追加续写 ，f 为对象名字
    #   写入文本形式的link
    i+=1;
    browser.find_element_by_link_text('下一章').click();
    #   根据文本找到元素，点击

browser.close();