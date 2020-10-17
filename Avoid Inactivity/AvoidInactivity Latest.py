import time
#import win32api
import pyautogui
import random, string, datetime
from idle_time import IdleMonitor

chk_for_min = 120
check_interval_sec = 30

inactivity_check = int (chk_for_min * 60 / check_interval_sec)
toggle_screen_check = int(900 / check_interval_sec)

monitor = IdleMonitor.get_monitor()

y = 1

try:
    for i in range(inactivity_check+1):
        #change tab of browser
        if monitor.get_idle_time() > check_interval_sec:
            #print (monitor.get_idle_time())
            pyautogui.hotkey('ctrl','tab')
        #else:
            #print (monitor.get_idle_time())
            #print ('No action taken')
        #change window
        if i + 1 == (toggle_screen_check * y)+1:
            pyautogui.hotkey('alt','tab')
            pyautogui.click(738,425)
            pyautogui.hotkey('alt','tab')
            y = y + 1
            print (('Switched screens at {} attempt').format(i+1))
        #else:
            #print ('Did not switch screens')

        time.sleep(check_interval_sec) if i+1 < inactivity_check + 1 else print ('Ending program')

except KeyboardInterrupt:
    print('Stopped')