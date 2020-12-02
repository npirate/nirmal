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
#click js
x_jscenter, y_jscenter = pyautogui.center(pyautogui.locateOnScreen('js2.png'))
pyautogui.click(x_jscenter, y_jscenter)

#wait for the blank area to appear
time.sleep(1)

#click in blank area
x_updatecenter, y_updatecenter = pyautogui.center(pyautogui.locateOnScreen('update.png'))
#pyautogui.moveTo((x_jscenter + x_updatecenter)/ 2, (y_jscenter + y_updatecenter)/ 2, duration = 0.2)
pyautogui.click((x_jscenter + x_updatecenter)/ 2, (y_jscenter + y_updatecenter)/ 2)    

#type the js code
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('delete')
pyautogui.typewrite('''function copyToClipboard(text){
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
    dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);}''')
pyautogui.hotkey('enter')
call_function = '''copyToClipboard (document.getElementById("type-text").innerText.replace(/(\\r\\n\\t|\\n|\\r\\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\\r\\n\\t|\\n|\\r\\t)/gm,""))'''
pyautogui.typewrite (call_function)

#inject js code and execute by clicking update
pyautogui.click(x_updatecenter, y_updatecenter)

time.sleep(1)

#pyautogui.typewrite ('''copyToClipboard (document.getElementById("type-text").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\r\n\t|\n|\r\t)/gm,""))''')

##pyautogui.PAUSE = 0.5
##pyautogui.FAILSAFE = True
###width, height = pyautogui.size()
##x_1min, y_1min = 825, 285
##pyautogui.click(x_1min, y_1min)
##pyautogui.moveTo(825, 370, duration=0.1)
##pyautogui.click(825,370)
##
##pyautogui.hotkey('ctrl', 'shift','j')
###pyautogui.hotkey ('f12')
###pyautogui.moveTo (85,585)
##time.sleep(2)
###pyautogui.typewrite('test')
##pyautogui.typewrite('''function copyToClipboard(text){
##    var dummy = document.createElement("input");
##    document.body.appendChild(dummy);
##	dummy.setAttribute('value', text);
##    dummy.select();
##    document.execCommand("copy");
##    document.body.removeChild(dummy);
##	}''')
###x, y = pyautogui.position()
###print (x, y )
##pyautogui.hotkey('enter')
##time.sleep (2)
##pyautogui.typewrite ('''copyToClipboard (document.getElementById("type-text").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\r\n\t|\n|\r\t)/gm,""))''')
##pyautogui.hotkey('enter')
##time.sleep (3)
##pyautogui.hotkey('f12')


#get input
#decide what to replace, and typing speed
#format input - remove new line, replace char at random
#select location to type
#type

##print ('''function copyToClipboard(text){
##    var dummy = document.createElement("input");
##    document.body.appendChild(dummy);
##	dummy.setAttribute('value', text);
##    dummy.select();
##    document.execCommand("copy");
##    document.body.removeChild(dummy);
##	}
##	
##	copyToClipboard (document.getElementById("type-text").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\r\n\t|\n|\r\t)/gm,""))''')


#letter = input ("Letter to Type: ")
letter = pyperclip.paste()
#letter = letter.replace('. ','.')
#letter = letter.replace('.','. ')
#letter = letter.replace(', ',',')
#letter = letter.replace(',',', ')
letter = letter.replace('! ','!')
letter = letter.replace('!','! ')
letter = letter.replace('? ','?')
letter = letter.replace('?','? ')
letter = letter.replace(': ',':')
letter = letter.replace(':',': ')



pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('here.png')))

#print (letter.replace(original,replaced_by))
letter = letter.replace(original,replaced_by)
#time.sleep(5)
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
