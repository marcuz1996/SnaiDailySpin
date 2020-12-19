# Daily Spin Script

## Description
This python script runs automatically the daily-spin-game of the Snai website and sends both the game result and the updated credit on Telegram chat through a bot.  
To do this it uses Telegram and Selenium modules.

## Setup
1. Install on the device which run the scipt, the Selenium and the Telegram modules.  
Selenium: ```pip install selenium```  
Telegram: ```pip install python-telegram-bot```
2. Configure users.txt: for each user add a line that contains ```username password nickname``` for example:  
```
admin Password123! administrator
root Psw987@ Boss
```
3. Put chromedriver.exe in Browser_Selenium folder. Download the correct version for your browser at this link: https://chromedriver.chromium.org/downloads
4. edit dailySpin.py Macro  
TOKEN : put the string corresponding to your bot's token  
CHAT_ID : put the chat id integer corresponding to your bot's (it has '-' before the numbers)
### Telegram setup
1. Create a bot with BotFather.
2. After creation you find the token in the chat.
3. Create a gruop with bot.
4. send this message ```/my_id@BotName```.
5. Go to following url: https://api.telegram.org/botXXX:YYYY/getUpdates where XXX:YYYY is the token of your bot.
6. Look for ```"chat":{"id":-zzzzzzzzzz, ``` where -zzzzzzzzzz is your chat id
