from operator import truediv
import pyautogui as auto
import time
""""
auto.press('win')
auto.write('fir')
auto.press('enter')
time.sleep(1.5)
auto.write('web.telegram.org' ,.2)
auto.press('enter')
auto.moveTo(245,22,2)
auto.click()
auto.write('toph.co',.2)
auto.press('enter')
time.sleep(.5)
auto.hotkey('ctrl','t')
time.sleep(.5)
auto.write('facebook.com',.2)
auto.press('enter')
auto.moveTo(79,747,2)
auto.click()
auto.moveTo(74,446,2)
auto.click()
auto.moveTo(241,421,2)
auto.click(None,None,2)
auto.moveTo(440,256,2)
auto.click()
auto.press('delete')
time.sleep(.5)
auto.press('enter')

#new tab func::
x = auto.locateCenterOnScreen('new.png', confidence=.06)
newTab = auto.locateCenterOnScreen('new.png',confidence=.7)
print(newTab)
auto.moveTo(newTab,None,5)

time.sleep(2)
toph=auto.locateCenterOnScreen('toph.png',confidence=.9)
auto.moveTo(toph,None,4)

#close func::
c=auto.locateCenterOnScreen('close.png',confidence=.8)
print(c)
auto.moveTo(c)

#massage box
auto.alert(text="This is button",title="BUTTON",button='ok')

#returns value
auto.confirm(text="this is confirm",title="confirm",buttons=['Ok','cencel'])

#prompt
email = auto.prompt(text="Email\Mobile:",title="Info desk")
pas = auto.password(text="Enter your password:",title="Info desk", mask="#")
"""
# time.sleep(3)
# n=auto.locateCenterOnScreen('like.png')
# auto.moveTo(n)
print(auto.size())