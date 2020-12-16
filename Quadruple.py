# import built-in modules
import os
import time
import subprocess

import argparse

# import browser modules
from selenium import webdriver
from pyvirtualdisplay import Display

# import core modules
from core import WB_login
from core import WB_tools
from core import style

# config values
cwd = os.getcwd()
coreDir = "core"
logsDir = "logs"
scanHttpServerDir = "scan"
wpChatUrl = 'https://web.whatsapp.com/send?phone='
VERSION = "1.0"

# Define args
parser = argparse.ArgumentParser(description='Developed By HDMX.')
parser.add_argument('-cf', '--check-files', action='store_true', help='check dirs and files needed by the script.')
parser.add_argument('-n', '--number', type=str, metavar='', help='provide target number with country code.')
parser.add_argument('-m', '--monitor', action='store_true', help='monitor the number when it\'s online and when it\'s not, then save the logs.')
parser.add_argument('-swo', '--send-when-online', type=str, metavar='', help='specify a msg string to send when the target is online.')
parser.add_argument('-ss', '--sticker-spammer', action='store_true', help='spam the first sticker from the recent ones n times [n by default is 200].')
parser.add_argument('-sn', '--sticker-number', type=str, metavar='', help='specify a number to spam the sticker n times [n by default is 200].')
parser.add_argument('-mb', '--msg-bommer', action='store_true', help='send a msg n times to the target or a text file line by line .')
parser.add_argument('-ms', '--msg-string', type=str, metavar='', help='specify a msg string to send to the target n times [n by default is 100].')
parser.add_argument('-mf', '--msg-file', type=str, metavar='', help='specify a file to send line by line to the target.')
parser.add_argument('-mn', '--msg-number', type=str, metavar='', help='specify a number of msgs to send to the target n times [n by default is 100].')
parser.add_argument('-v', '--version', action="store_true", help="show software version.")
args = parser.parse_args()


def show_version():
    exit(style.greenPlus + f"QuadrupleWhatsapp version {VERSION}")


def checkFiles():
    # check necessary dirs and files
    directories = [
        f"{coreDir}",
        f"{logsDir}",
        f"{coreDir}/{scanHttpServerDir}",
    ]

    coreFiles = [
        f"{coreDir}/WB_login.py",
        f"{coreDir}/WB_tools.py",
        f"{coreDir}/WB_httpServer.py",
        f"{coreDir}/WB_config.py",
        f"{coreDir}/style.py"
    ]

    for directory in directories:

        if os.path.exists(directory):
            print(style.greenPlus + directory + " exists.")
        else:
            print(style.redMinus + directory + " doesn't exist.")

    for file in coreFiles:

        if os.path.exists(file):
            print(style.greenPlus + file + " exists.")
        else:
            print(style.redMinus + file + " doesn't exist.")
    exit()


def filterPhoneNumber(phone):
    # reformat entered phone
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newPhone = ""
    for char in phone:
        if char in numbers:
            newPhone += char
    return str(newPhone)


def checkIfPhoneExists():
    # check if phone has whatsapp account
    print(style.greenPlus + 'Checking Phone Number')
    time.sleep(10)
    numberValidity = 0

    try:
        pageSource_ = driver.page_source
        soup_ = BeautifulSoup(pageSource_, features="lxml")
        invalidDivs = soup_.findAll("div", {"class": "_9a59P"})

        if len(invalidDivs) == 1:
            numberValidity = 0
    except:
        numberValidity = 1
        print(style.greenPlus + "Valid Phone Number")
        style.wipe()

    if numberValidity == 0:
        print(style.redMinus + "Invalid Phone Number")
        exit()


if __name__ == "__main__":

    if args.check_files is True:
        checkFiles()

    if args.version is True:
        show_version()

    if args.number is None:
        exit(style.redMinus + "please provide a number with a country code")

    style.wipe()
    print('\n' + style.greenPlus + 'Opening selenium webdriver ..')

    subprocess.Popen(["python3", f"{coreDir}/WB_httpServer.py"])

    # Hide the driver
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Firefox()

    WB_login.driver, WB_tools.driver = driver, driver
    WB_login.Login()

    style.wipe()

    phone = filterPhoneNumber(args.number)
    print(style.greenPlus + 'Getting Chat')
    driver.get(wpChatUrl + str(phone))
    time.sleep(.5)
    checkIfPhoneExists()

    logFile = f"{logsDir}/{phone}-log.txt"

    if args.monitor is True and args.sticker_spammer is True \
            or args.monitor is True and args.msg_bommer is True \
            or args.sticker_spammer is True and args.msg_bommer is True:

        print(style.redMinus + "can't do both at the same time.")

    if args.monitor is True:

        if args.send_when_online is not None:
            WB_tools.Tools.msgString = args.send_when_online

        WB_tools.logFile = logFile
        WB_tools.filteredPhoneNumber = phone
        WB_tools.Tools("monitorStatus")

    if args.sticker_spammer is True:
        if args.sticker_number is not None:
            WB_tools.Tools.numberOfStickers = int(args.sticker_number) + 1
        WB_tools.Tools("stickerSpammer")

    if args.msg_bommer is True:

        if args.msg_number is not None:
            WB_tools.Tools.mbNumber = int(args.msg_number)

        if args.msg_string is not None:
            WB_tools.Tools.mbMode = "string"
            WB_tools.Tools.msgString = args.msg_string

        if args.msg_file is not None:
            WB_tools.Tools.mbMode = "file"
            WB_tools.Tools.mbPath = args.msg_file

        WB_tools.Tools("msgBoomer")

    driver.quit()
