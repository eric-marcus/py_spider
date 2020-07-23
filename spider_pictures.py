from selenium import webdriver
from bs4 import BeautifulSoup
import requests


#批量获取图片并下载

url = 'http://www.yingyudd.com/shuben/beishida/3A/3.html';
browser = webdriver.Chrome();
browser.get(url);   #打开url

i = 2
while i < 82 :
    html = BeautifulSoup(browser.page_source , 'html.parser')   #获取网页html , 其中html.parser表示用html解析
    link = html.find('img' , {'id' : 'shubenimg'})      #查找标签为img,id为shubenimg的语句
    #  <img id="shubenimg" src="http://www.100875.com.cn:1314/data/upload/2014xxyy3q/xxyy3q3s/xxyy3q3s003.jpg" width="100%"/>
    print(link.get('src'))

    with open('pict/{}.{}'.format(i ,link.get('src')[len(link.get('src'))-3: len(link.get('src'))]),'wb') as jpg:
        jpg.write(requests.get(link.get('src')).content)
    i+=1
    browser.find_element_by_link_text('下一页>>>').click()

browser.close();
