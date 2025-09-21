import pyautogui as pag
import time

def screenshot(sx, sy, ex, ey):
    pag.hotkey("win", "shift", "s")
    time.sleep(0.1)
    pag.moveTo(sx, sy)
    time.sleep(0.2)
    pag.mouseDown()
    time.sleep(0.2)
    pag.moveTo(ex, ey)
    time.sleep(0.2)
    pag.mouseUp()
    time.sleep(1)

def letterToIndex(c):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    return letters.index(c)