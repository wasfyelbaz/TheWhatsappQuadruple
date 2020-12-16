# import built-in modules
from os import system
from time import sleep

# import browser modules
from selenium import webdriver
import selenium.common.exceptions
from bs4 import BeautifulSoup

# import core modules
from core import style
from core import WB_config

# import qrcode module
import qrcode


class Login:

    driver = None
    qrImgName = "core/scan/WB_qr.png"
    wpUrl = 'https://web.whatsapp.com/'

    def __init__(self):

        print('\n' + style.greenPlus + 'Connecting to WP Server ..')
        driver.get(self.wpUrl)
        sleep(3)
        print('\n' + ' Go to http://[MACHINE_IP]:6969 !')
        print(' Scan QR code with your phone !\n')

        self.checkLogin()

    def getQrValue(self):

        html = driver.page_source
        soup = BeautifulSoup(html, features="lxml")
        qrElement = soup.find(WB_config.qrElementName, {"class": WB_config.qrElementClassName})

        try:
            qrValue = qrElement[WB_config.qrElementValueAttr]
        except TypeError:
            qrValue = 0

        return qrValue

    def makeQrCode(self, data):

        qr = qrcode.QRCode(
            version=1,
            box_size=5,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color="white")
        img.save(self.qrImgName)

    def checkLogin(self):

        loop = True

        try:
            qrData = self.getQrValue()
        except KeyError:
            sleep(3)
            qrData = self.getQrValue()

        self.makeQrCode(qrData)

        while loop is True:

            html = driver.page_source
            soup = BeautifulSoup(html, features="lxml")
            myDivs = soup.findAll("div", {"class": "landing-title"})

            if len(myDivs) == 0:
                style.wipe()
                loop = False
                system('rm ' + self.qrImgName)
            elif len(myDivs) == 1:
                pass

            try:
                _qrData_ = self.getQrValue()
            except KeyError:
                loop = False
                system('rm ' + self.qrImgName)

            if _qrData_ == qrData:
                pass
            else:
                qrData = _qrData_
                self.makeQrCode(qrData)

            sleep(2)

        print(style.greenPlus + 'Logged in Successfully !')
        sleep(1)
