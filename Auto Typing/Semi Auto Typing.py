#pip install pyautogui
import pyautogui
import string
import random
import pyperclip #pip install pyperclip
import time

original = random.choice(string.ascii_uppercase)
replaced_by = random.choice(string.ascii_letters)
print ('Will replace: ', original, ' with ', replaced_by)

delay = input ("Give delay duration. Should not be more than 0.2: ")

letter = input ("Letter to Type: ")
#letter = pyperclip.paste()
#letter = letter.replace('. ','.')
#letter = letter.replace('.','. ')
#letter = letter.replace(', ',',')
#letter = letter.replace(',',', ')
#letter = letter.replace('! ','!')
#letter = letter.replace('!','! ')
#letter = letter.replace('? ','?')
#letter = letter.replace('?','? ')
#letter = letter.replace(': ',':')
#letter = letter.replace(':',': ')



#pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('here.png')))

#print (letter.replace(original,replaced_by))
letter = letter.replace(original,replaced_by)
print ('go to typing screen')
time.sleep(7)
pyautogui.typewrite (letter,delay) #more delay, lesser the speed
pyautogui.hotkey ('enter')

##import time
##
##x = "Test"pyaed to have Ueeutogui.moveTo(825, 370
##y = 0
##while y <= len(x):
##  #os.system("clear")
##  print (x[:y])#prints in IDE
##  time.sleep(.2)
##  y = y+1
