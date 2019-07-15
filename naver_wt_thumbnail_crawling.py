#썸네일 가져오기

from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve

#저장 폴더 생성 (os 모듈)
#https://wikidocs.net/30 - 예외처리 방식
try:
    if not (os.path.isdir('python_image')):
        os.makedirs(os.path.join('python_image'))
except OSError !=errno.EEXIST:
    print("폴더 생성 실패!")
    exit()


html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1_list = soup.findAll('div', {'class':'col_inner'})

#웹툰 리스트
li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll('li')) #해당 부분 찾아서 li_list에 병합

#pprint(li_list)

for li in li_list:
    img = li.find('img') #img 태그 찾기 
    title = img['title']
    img_src = img['src']
    #print(title, img_src)

    title = re.sub('[^0-9a-zA-zㄱ-힗]', '', title) #글자가 아닌것은 ''로 치환
    #특수문자가 있으면 에러남 / re(replace) 모듈 사용
    #정규식 표현 따로 찾아서 공부
    
    urlretrieve(img_src, './python_image/'+title+'.jpg') #주소, 파일경로 + 파일명 + 확장자

    
