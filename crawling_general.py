import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pytz import timezone

url = 'http://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000' # 일반공지

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
table = soup.find(id="board_list")
rows = table.find_all('tr')[1:]

# 상단 고정 공지 제외
today = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
# today = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d') # For test

start = 0
end = 0
for i in rows:
    if i.td.img is None:
        if today == i.select('td')[3].text.strip():
            end += 1
    else:
        start += 1

end += start
today_notice = rows[start:end]

# 오늘 올라온 공지 url
today_notice_url = []
for i in today_notice:
    today_notice_url.append('http://www.dongguk.edu/mbs/kr/jsp/board/' + i.a['href'].strip())
