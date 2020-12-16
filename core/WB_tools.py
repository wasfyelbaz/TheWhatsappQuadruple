# import built-in modules
import time
from os import system
from datetime import datetime

# import browser modules
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# import core modules
from core import style
from core import WB_config


class Tools:

    logFile = None
    filteredPhoneNumber = None
    driver = None
    numberOfStickers = None
    status = ''

    msgString = None
    mbMode = None
    mbPath = None
    mbNumber = 100

    def __init__(self, mode):

        self.mode = mode

        if mode == 'monitorStatus':
            handleFile = open(logFile, 'w')
            handleFile.write('Tracking Started ...')
            handleFile.close()

            self.checkStatus()

        elif mode == 'stickerSpammer':
            self.stickerSpammer()

        elif mode == 'msgBoomer':
            self.msgBoomer(self.mbMode, self.msgString, self.mbPath, self.mbNumber)

    def cycle(self):

        global status
        soup = BeautifulSoup(driver.page_source, features="lxml")
        myDivs = soup.findAll("span", {"title": "online"})

        if len(myDivs) == 0:
            self.status = 'offline'
        elif len(myDivs) == 1:
            self.status = 'online'

    def getTime(self):

        current_datetime = datetime.now()
        current_datetime = str(current_datetime).split(".")[0] + " UTC"
        return current_datetime

    def getLastLine(self, mode):

        with open(logFile, 'r') as f:
            lines = f.read().splitlines()
            lastLine = ''
            if mode == 0:
                lastLine = lines[-1]
            elif mode == 1:
                lastLine = lines[-2]
            return lastLine

    def checkStatus(self):

        try:

            while True:

                currentTime = self.getTime()
                lastLine = self.getLastLine(0)

                self.cycle()
                style.wipe()

                color = ''

                handleFile = open(logFile, 'a+')

                if self.status == 'offline':
                    color = style.Red

                    if '[OFFLINE]' not in lastLine:
                        handleFile.write('\n[OFFLINE] Since >> ' + str(currentTime))

                elif self.status == 'online':
                    color = style.Green

                    if '[ONLINE]' not in lastLine:
                        handleFile.write('\n[ONLINE] Since >> ' + str(currentTime))
                        # is online
                        if self.msgString is not None:
                            self.sendMsg(self.msgString)
                            time.sleep(1.5)
                            driver.quit()
                            exit()

                print(' '*25 + '[Number]: ' + style.Green + filteredPhoneNumber + style.Reset)
                print(' '*25 + '[Status]: ' + color + self.status + style.Reset)
                print(' '*25 + str(lastLine))

                handleFile.close()

        except KeyboardInterrupt:

            driver.quit()
            handleFile.close()
            style.wipe()
            print('*Activity Logs*')
            system('cat ' + logFile)
            print('\n')

    def stickerSpammer(self):

        if self.numberOfStickers is None:
            self.numberOfStickers = 5

        style.wipe()

        emojiBtn = driver.find_elements_by_class_name(WB_config.emojiBtnClassName[0])[1]
        emojiBtn.click()
        time.sleep(3)

        try:
            stickerBtn = driver.find_elements_by_class_name(WB_config.stickerBtnClassName)
            stickerBtn[3].click()
        except:
            time.sleep(3)
            stickerBtn = driver.find_elements_by_class_name(WB_config.stickerBtnClassName)
            stickerBtn[3].click()
        time.sleep(3)

        firstSticker = driver.find_elements_by_class_name(WB_config.firstStickerClassName)

        srickersSent = 0

        try:
            for i in range(self.numberOfStickers):
                firstSticker[0].click()
                print(f"{style.Green}*{style.Reset} Sending sticker number[{style.Red + str(srickersSent) + style.Reset}]")
                srickersSent += 1

        except KeyboardInterrupt:
            driver.quit()

    def msgBoomer(self, mode, string, path, n):

        textBox = driver.find_elements_by_class_name(WB_config.textBoxClassName)[1]
        global msgsSent
        msgsSent = 1

        def sendMsg(msg):

            textBox.send_keys(msg)
            textBox.send_keys(Keys.RETURN)
            time.sleep(.07)

        if mode == "string":
            for i in range(n):
                sendMsg(string)
                print(f"{style.Green}*{style.Reset} Sending msg number[{style.Red + str(msgsSent) + style.Reset}]")
                msgsSent += 1

        elif mode == "file":
            with open(path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    sendMsg(line)
                    print(f"{style.Green}*{style.Reset} Sending msg number[{style.Red + str(msgsSent) + style.Reset}]")
                    msgsSent += 1

    def sendMsg(self, msg):

        textBox = driver.find_elements_by_class_name(WB_config.textBoxClassName)[1]
        textBox.send_keys(msg)
        textBox.send_keys(Keys.RETURN)

        print(f"{style.Green}*{style.Reset} Sending msg '{msg}'")
