from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

url = "https://sparxmaths.uk/"

username = "ethancingapagu"
password = "fishnchips"
schoolName = "brighton college abu dhabi"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)

studentLogin = driver.find_element(By.LINK_TEXT, 'Student login')
studentLogin.click()
time.sleep(2)

pag.typewrite(schoolName, interval=0.02)
pag.press("enter")
pag.press("enter")

time.sleep(2)
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

homeworkAccordion = driver.find_elements(By.XPATH, "//span[contains(text(), 'Homework due Wednesday')]")[0]
homeworkAccordion.click()
time.sleep(5)
startBtn = driver.find_elements(By.XPATH, "//div[contains(text(), 'Start')]")[0]
startBtn.click()

time.sleep(2)

pag.hotkey("win", "shift", "s")
pag.moveTo(100, 322)
time.sleep(0.1)
pag.mouseDown()
time.sleep(0.1)
pag.moveTo(880, 930)
time.sleep(0.1)
pag.mouseUp()

time.sleep(122)
