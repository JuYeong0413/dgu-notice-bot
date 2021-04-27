# dgu-notice-bot
[![run-discord-bot](https://github.com/JuYeong0413/dgu-notice-bot/actions/workflows/workflow.yml/badge.svg?branch=main)](https://github.com/JuYeong0413/dgu-notice-bot/actions/workflows/workflow.yml)  
:elephant: 동국대학교 일반/학사/장학공지 디스코드 봇 ([채널 입장하기](https://discord.gg/XUhKUdA7Yx))  
  
동국대학교 제53대 경영대학 학생회 [동경]에서 코로나19 사태로 인해 학교에 대한 정보를 얻기가 쉽지 않은 상황을 고려해
학사/장학 관련 정보 전달에 적극적으로 임하고자 개설한 [카카오톡 오픈채팅방](https://open.kakao.com/o/gxsRLaOc)
으로부터 아이디어를 얻어 제작한 디스코드 봇.  
  
월, 수, 금요일마다 학생회에서 직접 오픈채팅방에 메시지를 남기는 번거로움을 해결하기 위해 평일 오후 6시에 당일 올라온
동국대학교 홈페이지의 일반/학사/장학 공지를 봇이 알려준다.  

## Environment
* Python 3.8.2
* beautifulsoup4
* requests
* [discord.py](https://github.com/Rapptz/discord.py)
* [html5lib](https://github.com/html5lib/html5lib-python)
* GitHub Action

## Running the server locally
1. Clone this repository.
```terminal
$ git clone https://github.com/JuYeong0413/dgu-notice-bot.git
```
2. Add Discord bot token in `secrets.json`.
```json
{
    "token": "Enter Your Discord Bot Token"
}
```
3. Install the requirements.
```terminal
$ pip3 install -r requirements.txt
```
4. Install `discord.py`
```terminal
$ python3 -m pip install -U discord.py
```
5. Run `discord_bot.py` file.
```terminal
$ python3 discord_bot.py
```
