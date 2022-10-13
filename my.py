import pyautogui as auto
import time
from liveScreen import points
import keyboard
def openFirfox():
    fir=points('firefox.png',.7)
    if fir is 0:
        win=points('win.png',.7)
        if win is 0:
            print("Cannot find firefox/start menu")
            exit()
        else:
            auto.moveTo(win,None,1)
            auto.click()
            auto.write('fir',.06)
            auto.press('enter')
            time.sleep(5)
    else:
        auto.moveTo(fir,None,1)
        auto.click()
        time.sleep(2)
def openNewTab():
    new=points('new.png',.4)
    auto.moveTo(new,None,4)
    auto.click()
def KeepScrol():
    auto.scroll(-40,None,None,None,_pause=False)
    time.sleep(.3)
def loveReact(react_img=None):
    #infinite loop,press 'c' to stop
    
    if react_img is None:
    #in default it searches for like image, hovers over it, waits for a bit, then reacts love.
    #in other words, reacts love on fb posts by default,
        while True:
            if keyboard.is_pressed("c"):
                break
            like=points('like.png',.9)
            while like==0:
                if keyboard.is_pressed("c"):
                    print("DONE!")
                    break
                print("like_img not found,retrying...")
                KeepScrol()
                like=points('like.png')
                if like!=0:
                    print("Like_img found after scrolling...")
                    auto.moveTo(like,None,1)
                    print("moved to like,line 45")
                    time.sleep(3)
                    love=points('love.png',.6)
                    while love == 0:
                        if keyboard.is_pressed("c"):
                            print("DONE!")
                            break
                        print("love_img not found,retrying...line 52")
                        time.sleep(3)
                        love=points('love.png',.6)
                        if love !=0:
                            print("love_img found ...line 56")
                            auto.moveTo(love,None,1)
                            auto.click()
                            like=0
                            if keyboard.is_pressed("c"):
                                print("DONE!")
                                break
                            time.sleep(1)
                    else:
                        print("love_img found on first attempt,line 65")
                        auto.moveTo(love,None,1)
                        auto.click()
                        like=0
                        if keyboard.is_pressed("c"):
                            print("DONE!")
                            break
                        time.sleep(1)
            else:
                print("like_img found on first attemp")
                auto.moveTo(like,None,1)
                if keyboard.is_pressed("c"):
                    print("DONE!")
                    break
                time.sleep(3)
                love=points('love.png',.6)
                while love == 0:
                    if keyboard.is_pressed("c"):
                        print("DONE!")
                        break
                    print("love_img not found,retrying...line 85")
                    time.sleep(3)
                    love=points('love.png',.6)
                    if love !=0:
                        print("love_img found ...line 89")
                        auto.moveTo(love,None,1)
                        auto.click()
                        like=0
                        if keyboard.is_pressed("c"):
                            print("DONE!")
                            break
                        time.sleep(1)
                else:
                    print("love_img found on first attempt,line 98")
                    auto.moveTo(love,None,1)
                    auto.click()
                    like=0
                    if keyboard.is_pressed("c"):
                        print("DONE!")
                        break
                    time.sleep(1)
    #need to react other than love? pass in png sample of that react.
    else:
        while True:
            if keyboard.is_pressed("c"):
                break
            react=points(react_img,.7,(243,314,501,345))
            while react==0:
                if keyboard.is_pressed("c"):
                    print("DONE!")
                    break
                print("react_img not found,retrying...")
                KeepScrol()
                react=points(react_img,.7,(243,314,501,345))
                if react!=0:
                    print("react_img found after scrolling...")
                    auto.moveTo(react,None,1)
                    react=0
                    auto.click()
                    if keyboard.is_pressed("c"):
                        print("DONE!")
                        break
def goto(_url):
    auto.write(_url,.08)
    auto.press('enter')
def moveTocenter():
    w,h=auto.size()
    center_x= w/2
    center_y=h/2
    auto.moveTo(center_x,center_y,1)

openFirfox()
openNewTab()
goto('facebook.com')
time.sleep(1)
moveTocenter()
loveReact()
