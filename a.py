import threading
import time
import pyautogui
import os
import keyboard

def y():
    while True:
        if keyboard.is_pressed('Tab'):
            os._exit(0)

def x():
    # start_time = time.time()
    # stop_time = start_time + 10  # 10 segundos a partir do início
    while True: #time.time() < stop_time
        pyautogui.press("p")
        pyautogui.press("i")
        pyautogui.press("n")
        pyautogui.press("t")
        pyautogui.press("o")
        pyautogui.press("_")
        time.sleep(0.01)


pyautogui.hotkey('win', '6') 
threading.Thread(target=x).start()
threading.Thread(target=y).start()