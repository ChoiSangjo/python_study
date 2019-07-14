from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#documentation // https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#미세먼지 날씨 가져오기 
html = requests.get('https://search.naver.com/search.naver?query=날씨')
html.close()

soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'detail_box'})
data2 = data1.findAll('dd')

fine_dust = data2[0].find('span', {'class':"num"}).text
print("미세먼지: ", fine_dust)

ultra_fine_dust = data2[1].find('span', {'class':'num'}).text
print("초미세먼지: ", ultra_fine_dust)

ozone = data2[2].find('span', {'class':'num'}).text
print("오존지수: ", ozone)

