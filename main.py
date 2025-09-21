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

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

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

def openHw():
    homeworkAccordion = driver.find_elements(By.XPATH, "//span[contains(text(), 'Homework due Wednesday')]")[0]
    homeworkAccordion.click()
    time.sleep(5)
    startBtn = driver.find_elements(By.XPATH, f"//div[contains(text(), '{str(args.mode).capitalize()}')]")[0 + int(args.indexoffset)]
    startBtn.click()
    time.sleep(2)

def screenshotQuestion():
    utility.screenshot(100, 322, 880, 930)

def pasteToGauth():
    pag.hotkey("ctrl", "shift", "n")
    time.sleep(0.2)
    pag.typewrite("https://www.gauthmath.com/")
    pag.press("enter")
    time.sleep(7)
    pag.moveTo(610, 460)
    pag.hotkey("ctrl", "v")
    
    time.sleep(11)
    utility.screenshot(243, 522, 697, 952)
    time.sleep(0.1)

qid = ""

def saveScreenshotFromGauth():
    qidEl = driver.find_element(By.CSS_SELECTOR, "a[class*='_Selected_']")
    global qid
    qid = qidEl.text

    pag.screenshot(f"{qid}.png", [243, 522, 697, 952])
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
time.sleep(122)
