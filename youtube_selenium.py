#유튜브 키워드 검색 

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get("http://www.youtube.com/")

time.sleep(3)

#검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//*[@id="search"]') #브라우저 검사 > copy > xpath

#search 변수에 저장된 곳에 값을 전송
search.send_keys('파이썬 코딩')
time.sleep(1)

#search 변수에 저장된 곳에 엔터를 입력 (입력은 from selenium.webdriver.common.keys import Keys)
search.send_keys(Keys.ENTER)
