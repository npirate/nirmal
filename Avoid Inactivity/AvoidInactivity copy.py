import time
import win32api
import pyautogui
import random, string, datetime

#print ('imported')

inactivity_check = 10 #in minutes
check_interval_sec = 10
try:
    for i in range(inactivity_check):
        #print ('Attempt number ', i+1)
        if (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0 > (check_interval_sec):
            print ('Idle for {0} secnds'.format((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0))
            pyautogui.click(738,425)
            pyautogui.hotkey('ctrl','tab')
            #pyautogui.typewrite ((''.join(random.choices(string.ascii_letters + string.digits, k=20))),0.15)
            #time.sleep(1)
            #print ('Initiated activity')
        #else:
            #print ('Idle for {0} secnds'.format((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0))
            #print ('No action taken')
        #print ('sleeping at ', str(datetime.datetime.now()))
        pyautogui.hotkey('alt','tab') if (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0 > 30 else print ('Did not switch screens')
        time.sleep(check_interval_sec) if i+1 < inactivity_check else print ('End')

except KeyboardInterrupt:
    print('Stopped')
    