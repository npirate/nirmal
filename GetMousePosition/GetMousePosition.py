import pyautogui
import time
try:
    while True:
        x, y = pyautogui.position()
        print('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + '\n')
        time.sleep(5)
except KeyboardInterrupt:
    print ('done')
