from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import telegram
import datetime
#from selenium.webdriver.common.keys import Keys



PATH_CHROME = "Browser_Selenium/chromedriver.exe"
URL_GAME = "https://www.snai.it/play/games/1516"
URL_LOGIN = "https://www.snai.it/user"
TOKEN = ""
CHAT_ID = 
PATH_SCREENSHOT = "screenshot.png"


def login(usr, psw):
    #Create new session
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(PATH_CHROME, chrome_options=options)
    driver.implicitly_wait(10)
    #Go to login page
    driver.get(URL_LOGIN)
    #Insert username
    username = driver.find_element_by_id('edit-name')
    username.clear()
    username.send_keys(usr)
    #Insert password
    password = driver.find_element_by_name('pass')
    password.clear()
    password.send_keys(psw)
    #Remove cookies banner
    element = driver.find_element_by_class_name('cookie-consent-banner-inner')
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)
    #Submit credentials
    driver.find_element_by_id("edit-submit").click()
    try:
        driver.find_element_by_id('saldo_user')
        #NOW YOU ARE LOGGED
        return driver
    except NoSuchElementException:
        #LOGIN FAILED
        driver.quit()
        return False
    
def openGame(driver):
    #Go to the game page
    driver.get(URL_GAME)
    time.sleep(10)
    #Take screenshot
    driver.save_screenshot('screenshot.png')

    
def sendCredit(driver):
    #Go to user page
    driver.get(URL_LOGIN)
    bot = telegram.Bot(token=TOKEN)
    #Send message to telegram
    message = 'CREDITO RESIDUO: ' + driver.find_element_by_id('saldo_user').text
    bot.send_message(chat_id=CHAT_ID, text=message)

def sendScreenshot():
	bot = telegram.Bot(token=TOKEN)
    #Send photo to telegram
	bot.send_photo(chat_id=CHAT_ID, photo=open(PATH_SCREENSHOT, 'rb'),caption=str(datetime.datetime.now()))


def sendMessage(text_message):
    bot = telegram.Bot(token=TOKEN)
    #Send message to telegram
    bot.send_message(chat_id=CHAT_ID, text=text_message)


def createSession(usr, psw, nick):
    driver = login(usr, psw)
    if driver:
        print("[]LOGIN SUCCESSFUL")
        openGame(driver)
        openGame(driver)
        sendMessage(nick)
        sendScreenshot()
        sendCredit(driver)
        driver.quit()
    else:
        print ("[]LOGIN FAILED")


#MAIN
file = open('users.txt', 'r')
lines = file.readlines()
for line in lines:
    credential = line.split(' ')
    createSession(credential[0], credential[1], credential[2])