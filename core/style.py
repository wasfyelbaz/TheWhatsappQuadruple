from colorama import Fore, Style
from os import system

bold = '\033[1m'
Red = bold + Fore.RED
Green = bold + Fore.GREEN
Reset = Style.RESET_ALL + bold
greenPlus = Reset + ' [' + Green + '+' + Reset + '] '
redMinus = Reset + ' [' + Red + '-' + Reset + '] '

banner = """
 _______ _     _ _______                                                              
    |    |_____| |______                                                              
    |    |     | |______                                                              
                                                                                      
             _____  _     _ _______ ______   ______ _     _  _____         _______
            |   __| |     | |_____| |     \ |_____/ |     | |_____] |      |______
            |____\| |_____| |     | |_____/ |    \_ |_____| |       |_____ |______
                                                                        
                                                                          By: HDMX
                                                                        
"""

def wipe():

    system('clear')
    print(Green + banner + Reset)
