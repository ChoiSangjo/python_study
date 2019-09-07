import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

#LINE bot으로도 연습해보기

bot = telegram.Bot(token='977420791:AAFP5flh1wz0_hhl-NFLNAfkpndE9IGcWo0')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190907'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id = 642229581, text = title + 'IMAX 예매가 열렸습니다.')
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds = 30)
sched.start()