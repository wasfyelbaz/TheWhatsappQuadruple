![TheQuadruple](https://github.com/wasfyelbaz/TheWhatsappQuadruple/blob/main/core/logo.PNG)
## Dependencies
* Python3 Modules:
    * Selenium
    * pyvirtualdisplay
    * bs4
    * qrcode
    
* Linux OS (Kali is preferable) 

## Installation

    git clone git://github.com/wasfyelbaz/TheWhatsappQuadruple.git
    
    pip3 install -r requirements.txt

## Command line options
$ python3 Quadruple.py -h

*  `-cf`, `--check-files` check dirs and files needed by the script.

*  `-n`, `--number`          provide target number with country code.

*  `-m`, `--monitor`          monitor the number when it's online and when it's not, then save the logs.

*  `-swo`, `--send-when-online` specify a msg string to send when the target is online.

*  `-ss`, `--sticker-spammer` spam the first sticker from the recent ones n times [n by default is 200].

*  `-sn`, `--sticker-number` specify a number to spam the sticker n times [n by default is 200].

*  `-mb`, `--msg-bommer`    send a msg n times to the target or a text file line by line .

*  `-ms`, `--msg-string`   specify a msg string to send to the target n times [n by default is 100].

*  `-mf` , `--msg-file`     specify a file to send line by line to the target.

*  `-mn` , `--msg-number`   specify a number of msgs to send to the target n times [n by default is 100].

*  `-v`, `--version`        show software version.

## Features !

* Monitor the status ( online / offline ) of a specific phone number and log online history.
* Monitor a specific phone number until being online then send a customized message !
* Sticker Spammer : Spam the first sticker of the recently sent stickers n times to the target.
* Message Bommer : Send or (boom) a message n times to the target.

**Yes, you probably guessed why its name is "Quadruple" ...**

## Usage

1. Using the first feature **[Monitoring]**

    `python3 Quadruple.py --number (1)-123-xxx-xxxx --monitor`
     ##### Note: Don't worry about phone formatting, any char except from 0-9 will automatically be excluded.

2. Using the second feature **[Send a message once online]**

    `python3 Quadruple.py --number (1)-123-xxx-xxxx --monitor -send-when-online "MsgString"`
     ##### Note: it's better to put double quotes around message string.

3. Using the third feature **[Sticker Spammer]**

    `python3 Quadruple.py --number (1)-123-xxx-xxxx --sticker-spammer --sticker-number 50`
     ##### Note: By default the number of stickers to be sent is 200 if "--sticker-number" isn't specified.

4. Using the third feature **[Sticker Spammer]**
    
    `python3 Quadruple.py --number (1)-123-xxx-xxxx --msg-bommer --msg-string "MsgString" --msg-number 50`
     ##### Note: By default the number of messages to be sent is 100 if "--msg-number" isn't specified.
     or
    `python3 Quadruple.py --number (1)-123-xxx-xxxx --msg-bommer --msg-file path/to/the/file`
     ##### Note: Can't use "--msg-number" argument when using "--msg-file" argument.

## Disclaimer

* This tool is just for fun, you can have fun with your family and friends, however, you shouldn't use it to annoy people
and you take full responsibility towards your actions !

