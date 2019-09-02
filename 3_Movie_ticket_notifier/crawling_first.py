import requests
from bs4 import BeautifulSoup

#파이썬으로 영화 예매 오픈 알리미 만들기
#https://www.inflearn.com/course/%EC%98%81%ED%99%94%EC%98%88%EB%A7%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC/dashboard


#구현 아이디어
#1. op.gg/fow에서 친구들 아이디 여러개 입력해두면 최신 결과 정보를 메신저로 파싱하는 서비스
#2. 게임 할인 정보 메신저로 파싱하는 서비스
#3. 인스타그램에서 특정 태그 정보 파싱해주는 서비스

url = 'https://www.inflearn.com/'
html = requests.get(url)
print(html.text)
