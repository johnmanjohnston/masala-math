from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time
import utility
import argparse

parser = argparse.ArgumentParser(prog="main.py")
parser.add_argument("--mode", "-m", help="start or continue existing homework?")    
parser.add_argument("--indexoffset", "-i", help="offset index of question to be answered")
args = parser.parse_args()

url = "https://sparxmaths.uk/"

username = "ethancingapagu"
password = "fishnchips"
schoolName = "brighton college abu dhabi"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(1)

ypixeloffset = 54 # because of the "Chrome is being controlled by automated test software." thing

def auth():
    studentLogin = driver.find_element(By.LINK_TEXT, 'Student login')
    studentLogin.click()
    time.sleep(2)

    pag.typewrite(schoolName)
    time.sleep(0.1)
    pag.press("enter")
    time.sleep(0.2)
    pag.press("enter")
    time.sleep(0.1)
    pag.press("enter")

    time.sleep(3)
    pag.press("enter")
    time.sleep(2)
    pag.press("enter")

    rejectCookies = driver.find_element(By.XPATH, "//div[@id='cookiescript_reject']")
    rejectCookies.click()

    usernameField = driver.find_element(By.NAME, 'username')
    passwordField = driver.find_element(By.NAME, 'password')

    usernameField.send_keys(username)
    passwordField.send_keys(password)

    pag.press("enter")

    time.sleep(7)

    pag.hotkey("ctrl", "-")
    pag.hotkey("ctrl", "-")

def openHw():
    homeworkAccordion = driver.find_elements(By.XPATH, "//span[contains(text(), 'Homework due Wednesday')]")[0]
    homeworkAccordion.click()
    time.sleep(5)
    startBtns = driver.find_elements(By.XPATH, f"//div[contains(text(), '{str(args.mode).capitalize()}')]")[0 + int(args.indexoffset)]
    
    startBtns.click()
    time.sleep(2)

def screenshotQuestion():
    utility.screenshot(100, 290, 880, 930)

questionsCount = 0
def pasteToGauth():
    pag.hotkey("ctrl", "shift", "n")
    time.sleep(0.2)
    pag.typewrite("https://www.gauthmath.com/")
    pag.press("enter")
    time.sleep(7)
    pag.moveTo(550, 345 + ypixeloffset)
    pag.hotkey("ctrl", "v")
    
    time.sleep(11)

    global questionsCount
    if questionsCount < 1: 
        pag.hotkey("ctrl", "-")
        pag.hotkey("ctrl", "-")

    for _ in range(7): pag.press("down")

    time.sleep(0.1)

    questionsCount += 1

qid = ""

def saveScreenshotFromGauth():
    qidEl = driver.find_element(By.CSS_SELECTOR, "a[class*='_Selected_']")
    global qid
    qid = qidEl.text

    pag.screenshot(f"{qid}.png", region=(180, 165, 530, 790))
    time.sleep(2)

    pag.hotkey("alt", "tab")

    time.sleep(0.5)

def nextQuestion():
    index = utility.letterToIndex(qid[1])
    print(f"{index=}")
    parentEL = driver.find_elements(By.CSS_SELECTOR, "a[class^='_TaskItemLink']")[index+1]
    parentEL.click()

def main():
    auth()
    print(f"Logged in as {username}")
    openHw()

    numUnnatempted = len(driver.find_elements(By.CSS_SELECTOR, "a[class*='_Unattempted']")) + len(driver.find_elements(By.CSS_SELECTOR, "a[class*='Incorrect']"))
    print(f"{numUnnatempted=}")

    for _ in range(numUnnatempted):
        screenshotQuestion()
        pasteToGauth()
        saveScreenshotFromGauth()
        nextQuestion()
        time.sleep(1)

main()

x = input()