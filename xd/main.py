from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  682 Y:  480 RGB: (141, 197, 254)

#X:  772 Y:  480 RGB: ( 54, 159, 198)

#X:  859 Y:  480 RGB: (171, 216, 254)

#X:  930 Y:  480 RGB: (152, 183, 254)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(682,480)[0] == 1 or pyautogui.pixel(682,480)[0] == 0:
        click(682,480)
    if pyautogui.pixel(772,480)[0] == 1 or pyautogui.pixel(772,480)[0] == 0:
        click(772,480)
    if pyautogui.pixel(859,480)[0] == 1 or pyautogui.pixel(859,480)[0] == 0:
        click(859,480)
    if pyautogui.pixel(930,480)[0] == 1 or pyautogui.pixel(930,480)[0] == 0:
        click(930,480)
