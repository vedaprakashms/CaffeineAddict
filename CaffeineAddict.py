# This short script will keep mouse-clicking every 60 sec
# for n amount of minutes to not let computer fall asleep
# this is a modified code on top of the code found on the internet. 
import win32api, win32con, time, random, sys
from pynput.keyboard import Key, Controller



keyboard = Controller()
# Total time

MINUTES = int(sys.argv[1])


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

for i in range (0, MINUTES*3):
    if random.randint(0,100)% 2== 0:
        click(random.randint(30,55), 0)
        print("MM b 30 55")
        time.sleep(10)
        click(random.randint(70,90), 0)
        print("MM b 70 90")
        time.sleep(10)
    else:
        keyboard.press(Key.f14)
        keyboard.release(Key.f14)
        print("pressing f14")
        time.sleep(10)
        keyboard.press(Key.f15)
        keyboard.release(Key.f15)
        print("pressing f15")
        time.sleep(10)
        
