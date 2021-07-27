import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pytz import timezone
import re
import html5lib


def get_url_list(url):
    session = requests.Session()
    session.verify = False

    html = session.post(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    try:
        table = soup.find('table')
        rows = table.find_all('tr')[1:]
    except Exception as e:
        print(e)

    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y.%m.%d')
    # today = (datetime.today() - timedelta(days=1)).strftime('%Y.%m.%d') # For test

    today_notice = []
    for i in rows:
        if today == i.select('td')[3].text.strip():
            today_notice.append(i)
                
    # 오늘 올라온 공지 url
    today_notice_url = []
    for i in today_notice:
        today_notice_url.append('https://cse.dongguk.edu' + i.a['href'].strip())

    return today_notice_url


def get_notice_list(urls):
    notice_list = []
    for url in urls:
        session = requests.Session()
        session.verify = False

        html = session.post(url)
        soup = BeautifulSoup(html.text, 'html5lib')
        title_text = soup.select_one('.kboard-title > p').text.strip()
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
    url = 'https://cse.dongguk.edu/?page_id=799' # 컴퓨터공학과
    notice_type = "컴퓨터공학과 "
    
    print(run(url, notice_type))
