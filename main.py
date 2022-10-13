import pyautogui as auto
import time
i="I "
l="miss "
u="you "
time.sleep(3)
n=1
while n<=10:
    auto.typewrite(i+l+u+ str(n) + "!")
    auto.press('Enter')
    time.sleep(.2)
    n+=1