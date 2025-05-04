import pyautogui
import time

a = 1

while a <= 3:
    time.sleep(4)
    pyautogui.typewrite("Easin")

    time.sleep(2)
    pyautogui.press('enter')

    a = a + 1

