import pyautogui
import time
from pynput.keyboard import Controller
pynput_keyboard = Controller()

n = int(input())
l = [input() for _ in range(n)]

# cmd+shift+4 max num: 1440*900. pyautogui.screenshot(): 2880*1800.
# im = pyautogui.screenshot(region=(x, y, height, width))
# im.save("im.png")

pyautogui.click(1073, 327) # 타이핑 할 위치 클릭
pynput_keyboard.type("곰재줘 . . ASSEMBLE !!\n")
print("곰재줘 . . ASSEMBLE !!")

for i in range(1, n+1):
    pynput_keyboard.type("@"+l[i-1])
    print(i, l[i-1])
    time.sleep(0.5)

    im = pyautogui.screenshot(region=(1395*2, 180*2, 10*2, 70*2))
    px1 = im.getpixel((5*2, 5*2))
    px2 = im.getpixel((5*2, 65*2))
    if 53-5<px1[0]<53+5:
        pyautogui.click(1400, 185)
    elif 53-5<px2[0]<53+5:
        pyautogui.click(1400, 245)
    
    pynput_keyboard.type(" ")

    if i%10==0 or i==n:
        pynput_keyboard.type("\n")
        print("SEND")