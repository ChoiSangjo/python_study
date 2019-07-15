from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#웹툰 제목 가져오기

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
wsoup = bs(html.text, 'html.parser')
html.close()

#월요웹툰영역 추출하기
wdata1_list = wsoup.findAll('div',{'class':'col_inner'})

#제목 포함영역 추출하기
#wdata2=wdata1.findAll('a',{'class':'title'})

#텍스트 추출 1
#title_list = []
#for t in wdata2:
#    title_list.append(t.text)
#pprint(title_list)

#텍스트 추출 2
#title_list = [t.text for t in wdata2]
#pprint(title_list)

week_title_list = []

for wdata1 in wdata1_list:
    #제목 포함영역 추출
    wdata2 = wdata1.findAll('a',{'class':'title'})

    title_list = [t.text for t in wdata2]
    #pprint(title_list)
    #week_title_list.extend(title_list) #1차원 리스트로 만들려면 extend
    week_title_list.append(title_list) #2차원 리스트로 만들려면 append

pprint(week_title_list)



#코드를 줄이면 이렇게

#from bs4 import BeautifulSoup
#from pprint import pprint
#import requests

#html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
#soup = BeautifulSoup(html.text, 'html.parser')
#html.close()

#data1=soup.findAll('a',{'class':'title'})
#week_title_list = [ t.text for t in data1]
#pprint(week_title_list)

