from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#웹툰 제목 가져오기

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
wsoup = bs(html.text, 'html.parser')
html.close()

#월요웹툰영역 추출하기
wdata1=wsoup.find('div',{'class':'col_inner'})

#제목 포함영역 추출하기
wdata2=wdata1.findAll('a',{'class':'title'})

#텍스트 추출
title_list = []
for t in wdata2:
    title_list.append(t.text)

pprint(title_list)
