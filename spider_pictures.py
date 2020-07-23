from selenium import webdriver
from bs4 import BeautifulSoup
import requests

'''
获取图片并下载
url = 'http://www.yingyudd.com/shuben/beishida/3A/3.html';
browser = webdriver.Chrome();
browser.get(url);   
#   打开url

i = 2
while i < 82 :
    html = BeautifulSoup(browser.page_source , 'html.parser')
    #   获取网页html , 其中html.parser表示用html解析
    link = html.find('img' , {'id' : 'shubenimg'})
    #   查找标签为img,id为shubenimg的语句
    print(link.get('src'))
    #   <img id="shubenimg" src="http://www.100875.com.cn:1314/data/upload/2014xxyy3q/xxyy3q3s/xxyy3q3s003.jpg" width="100%"/>
    #   打印出获取的url信息

    with open('pict/{}.{}'.format(i,  link.get('src')[len(link.get('src'))-3: len(link.get('src'))]),  'wb') as jpg:
        jpg.write(requests.get(link.get('src')).content)
    #   with open 进行文件读写操作 ， ‘wb’ 二进制形式进行覆写 ， jpg 为对象名字
    #   with open 参数（文件存放地址/文件名。后缀名）  i 文件名 , 保留后3位的后缀名 ， ‘wb’
    #   写入下载的content
        
    i+=1
    browser.find_element_by_link_text('下一页>>>').click()
    #   根据文本找到元素，点击

browser.close();
'''
