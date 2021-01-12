# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import re
import json
import random
from selenium.webdriver.common.keys import Keys
from urllib .request import urlopen
from selenium.webdriver.common.action_chains import ActionChains


#登录
exr_data = r'D:\Program Files\360Chrome\Chrome\Application\360chrome.exe'
chrome_options = Options()
chrome_options.binary_location = exr_data
browser = webdriver.Chrome(chrome_options = chrome_options)

#driver.get("https://www.sxgbxx.gov.cn/login")
time.sleep(20)
browser.get("https://www.sxgbxx.gov.cn/front/showCourseList")

#课程列表
cou_url = "https://www.sxgbxx.gov.cn/front/showCourseList"
cou_html = urlopen(cou_url)

f1 = open('cou_url.txt','w')
f2 = open('cou_name.txt','w')
page = 0
while page < 35:
    cou_obj = BeautifulSoup(browser.page_source,"lxml")
    cou_list = cou_obj.findAll("a",{"class":"j-course-title"})
    
    print(page+1)
    for cou in cou_list:
    
        print(cou.get_text())
        print(cou['href'])
        
        
        f1.write(cou['href'])
        f1.write('\n')
        
        f2.write(cou.get_text())
               
        f2.write('\n')
    browser.find_element_by_id('nextpage').click()
    time.sleep(2)
    page += 1
f1.close()
f2.close()
browser.quit()


    




