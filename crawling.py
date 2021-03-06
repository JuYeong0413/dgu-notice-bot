import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pytz import timezone
import re
import html5lib


def get_url_list(url):
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

    return today_notice_url


def get_notice_list(urls):
    notice_list = []
    for url in urls:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html5lib')
        table = soup.find(id="board_view")
        title_text = table.select_one('th').text.strip()
        title = re.sub(r'\s+', ' ', title_text)
        notice_list.append({'title': title, 'url': url})
    return notice_list


def run(url, notice_type):
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y년 %m월 %d일')
    # today = (datetime.today() - timedelta(days=1)).strftime('%Y년 %m월 %d일') # For test

    urls = get_url_list(url)
    notice_list = get_notice_list(urls)

    str = ""
    result = []
    for notice_dict in notice_list:
        for k,v in notice_dict.items():
            if (len(str) > 1600):
                result.append(str)
                str = ""

            str = "{}\n{}".format(str, v)

            if k == 'url':
                str += "\n"

    if (str != ""):
        result.append(str)

    # Split long messages
    length = len(result)
    if (length > 0):
        for i in range(length):
            str = result[i]
            
            if i == 0:
                result[i] = ":bulb: {} {}공지입니다.\n{}".format(today, notice_type, str)
            else:
                result[i] = "_ _{}".format(str)

    else:
        str = ":bulb: {} {}공지는 없습니다.\n".format(today, notice_type)
        result.append(str)

    return result


if __name__ == "__main__":
    # test
    # url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000' # 일반공지
    # url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000' # 학사공지
    url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3662&id=kr_010804000000' # 장학공지

    # notice_type = "일반"
    # notice_type = "학사"
    notice_type = "장학"
    
    print(run(url, notice_type))
