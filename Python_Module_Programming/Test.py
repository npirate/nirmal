 ##number = 1
##limit = 6
##entry = str (input ('enter a word: '))
##for alpha in entry :
##    if number > limit:
##        break
##    if alpha == 'r':
##        pass
##        print ('cant print')
##        number += 1
##        limit +=1
##    else:
##        print ('alphabet ', number, 'in ', entry, 'is ', alpha)
##        number += 1    
##else:
##    print ('you did not enter anything')
    
##def Fibo ():    
####Fibonacchi sequence
##    start = 1
##    result = 1
##    previous_result = 0
##    try:
##        limit = int (input ('Enter length of Fibonacchi sequence: '))
##    
##        while start <= limit:
##            output = result + previous_result
##            previous_result = result
##            print (output)
##            result = output
##            start +=1
##        
##    except (ValueError, KeyboardInterrupt):
##        print ('You must enter a number')
##
####must not include whole code for exception handling. Bad practise

####Functions and arguments
##def hi(v1 = 'default v1', v2 = 'default v2'):
##    print (v1, ' and ', v2, ' are variables.')


####Raising Exception and Finally clause
##import sys
##try:
## ##raise ValueError
## print ('exception not raised and hence sys.exit will not execute')   
##except ValueError:
## print("ValueError Exception! handling occured")
## sys.exit ()
##finally:
##    print ('finally executed. So everything here will be executed before system closes down if exeption causes system to crash.')
##    
##print ('shows that exception didnt occur')

##def to_print():
##    print ('single quote')
##    print ("double quote       ")
##    print ("""triple quote
##on multiple lines""")

####fun with string
##s1 = 'Hello () World'
##s2 = 'Python is awesome '
##print(s1[6])
##print(s1[:10])
##print(s2[10:])
##s3 = s1[:6]+s2[7:]
##print (s3*3)

####find info in strings and format it using format () function
##s = 'Vijay Dinanath Chauhan sits next to me, yes, correct, next to me'
##print (s.find('Chauhan'))
##print (s.index('Chauhan'))
##
##f = '{:*^15.2f}'
##print (f.format (7000))

####lists
##list = ['One', 2, 'Three', 2, 2, 2, 2, 2, 2, 2, False]
##print (list[0:])
##print('Length = ',len (list))
##print (list[-3:])
###add '4' at third index position i.e fourth position
##list.insert(3,4)
##print (list[0:])
##print ('New length = ', len (list))
##list.pop()
##list.remove('Three')
##list.remove('One')
##list.append(3)
##list.append(1)
##print (list[0:])
##list.sort()
##for x in list:
##    print (x, end=' ')
##print ()
##print(list.count(2))


####List counter
##from collections import Counter
##list = ['a', 'b', 'c', 'd','a', 'b', 'c', 'd','a', 'b', 'c', 'd']
##listcount = Counter (list)
##print (listcount)
##for everyitem in listcount.items():
##    print ('Item: ', everyitem[0], 'Appears: ', everyitem[1], 'times')
##    print ('Item: ', everyitem[0], 'comes: {0} times'.format(listcount.get(everyitem[0])))
####everyitem[0] is the individual content of the list and everyitem[1] is its frequency
##print("The value 1 appears {0} times."
##         .format(listcount.get(everyitem[0])))
#### {0} is the placeholder and .format () function tells what comes there when script runs

####Tuple, immutable list
##tuple = ('Red', 'Blue')
##print (', '.join(tuple))# joins the elements of the tuple.', ' tells what will be there in between the two elements
##tuple = tuple.__add__(('Green',))
##print (tuple)
##tuple = tuple.__add__(('Shades', ('Orange', 'Yellow')))
##print (tuple[4][1])

####Dictionary
##barakhadi = {'ka': 'क', 'kha': 'ख', 'ga': 'ग'}
##print (barakhadi)
##print (barakhadi['kha'])
##barakhadi.update({'gha': 'घ'})
##print (barakhadi.keys())
##for alphabet in barakhadi.keys():
##    print ('{0} will be replaced by {1}'.format(alphabet,barakhadi[alphabet]))
    
####Dictionary as switch
###define the functions
##def PrintBlue():
## print("You chose blue!\r\n")
##def PrintRed():
## print("You chose red!\r\n")
##def PrintOrange():
## print("You chose orange!\r\n")
##def PrintYellow():
## print("You chose yellow!\r\n")
###assign key:value = key:function. So selecting the key will call the function and execute it.
##ColorSelect = {
## 0: PrintBlue,
## 1: PrintRed,
## 2: PrintOrange,
## 3: PrintYellow
##}
###this while statement will allow function to run over and over again till user wants to quit
##Selection = 0
##while (Selection != 4):
##     print("0. Blue")
##     print("1. Red")
##     print("2. Orange")
##     print("3. Yellow")
##     print("4. Quit")
###asks for selection and post selection calls the corresponding function
##     Selection = int(input("Select a color option: "))
##     if (Selection >= 0) and (Selection < 4):
##         ColorSelect[Selection]()

####list as stacks
##MyStack = []
##StackSize = 3
##def DisplayStack():
## print("Stack currently contains:")
## for Item in MyStack:
##     print(Item)
##
##def Push(Value):
## if len(MyStack) < StackSize:
##     MyStack.append(Value)
## else:
##     print("Yout tried pushing ", Value, " . But the stack is full!")
##def Pop():
## if len(MyStack) > 0:
##     MyStack.pop()
## else:
##     print("Stack is empty.")
##Push(1)
##Push(2)
##Push(3)
##DisplayStack()
##input("Press any key when ready...")
##Push(4)
##DisplayStack()
##input("Press any key when ready...")
###remove the last element from the stack
##Pop()
##DisplayStack()
##input("Press any key when ready...")
###push new element at end of list.
##Push(4)
##DisplayStack()

####queue - add/remove only from the end
##import queue
###fix length of queue
##MyQueue = queue.Queue(3)
##print('The queue is empty = ', MyQueue.empty())
##input("Press any key. It will add two elements in the queue...")
##MyQueue.put(1)
##MyQueue.put(2)
##print('The queue is full = ', MyQueue.full())
##input("Press any key. It will add one element in the queue...")
##MyQueue.put(3)
##print('The queue is full = ', MyQueue.full())
##print ('''now the queue is full.
##If you add one more element, it will not line up in the queue and so program will not progress till the element is added to the queue.
##Hence the script will hang''')
##input("Press any key. It will remove one element. will follow FIFO...")
##print(MyQueue.get())
##print('The queue is empty = ', MyQueue.empty())
##print('The queue is full = ', MyQueue.full())
##input("Press any key.Will remove two elements. will follow FIFO")
##print(MyQueue.get())
##print(MyQueue.get())

####deque - add/remove from both ends
##import collections
##MyDeque = collections.deque("abcdef", 10)
##print("Starting state:")
##for Item in MyDeque:
## print(Item, end=" ")
##print("\r\n\r\nAppending and extending right")
###add only one element
##MyDeque.append("h")
###add multiple elements
##MyDeque.extend("ij")
##for Item in MyDeque:
## print(Item, end=" ")
##print("\r\nMyDeque contains {0} items.".format(len(MyDeque)))
##print("\r\nRemoving from right")
##print("Removing {0}".format(MyDeque.pop()))
##for Item in MyDeque:
## print(Item, end=" ")
##print("\r\n\r\nAppending and extending left")
##MyDeque.appendleft("a")
##MyDeque.extendleft("bc")
##for Item in MyDeque:
## print(Item, end=" ")
##print("\r\n\r\nMyDeque contains {0} items. It removed i since we added 11th element from left and hence the extra element got removed from right".format(len(MyDeque)))
##
####class
##class newclass:
##    greeting = 'class variable' #this is class variable
##    def __init__(self, name='there'): # this will now define constructor
##        #constructor is a special method which is called by default everytime
##        #object is instantiated / created
##        #if no argument passed to the class, then uses default values of self.greeting which is value of variable 'name'
##        #if argument given at class level then it is passed to self.greeting via self and then that used
##        self.greeting = name + '!'    # self.greeting becomes instance variable
##           
##    def sayhello (self):
##        #if you pass argument here then error will occur since we have not programmed how that argument would be handled.
##        #but self tells function to use resources from constructor
##            print ('hello {0}'.format (self.greeting))
##
##instance = newclass()
##instance.sayhello()

####Instance variables
##class MyClass:
## def DoAdd(self, Value1=0, Value2=0):
##     Sum = Value1 + Value2 # all these are instance variables
##     print("The sum of {0} plus {1} is {2}.".format(Value1, Value2, Sum))
##instance = MyClass()
##instance.DoAdd (1, 4)

####unnamed and named argument list
##class newclass:
##    def list1(*args):# list of argument could be of any length
##        for x, y in enumerate(args):#enumerate() gets you individual values
##            print ('{0}. {1}'.format(x+1, y))
##
##    def list2(**kwargs):
##        for a, b in kwargs.items():
##            print ('{0} likes {1}'.format (a,b))
##        
##
##newclass.list1('Red', 'Blue', 'Green')
##newclass.list2 (George = 'Red', Sue = 'Green', Zarah = 'Blue')

####overloading operators. Overloading means over-riding the default working of anything that you are over-loading
##v1 = ("Red", "Green", "Blue")
##v2 = ("Yellow", "Purple", "Cyan")
##print("{0} + {1} = {2}".format(v1, v2, v1 + v2))
##print ('The above is default working of + operator. It has merged the two tuples. + doesnt work on objects. we need to define its working if we want to use it for objects.')
##
##
##class MyClass:
##    def __init__(self, *args):
##        self.Input = args #arguments stored in object called Input
##
##    def __add__(self, sumup):
##        #operators dont work on objects. so we define now as to how + should work with objects
##        Output = MyClass()
##        Output.Input = self.Input + sumup.Input
##        #anything given after + operator goes to sumup. Output object when instantiated got its resources (input object) from the __init__ method
##        return Output
##
##    def __str__(self):# __str__() converts object into string. It has to be an object to be converted. It can convert a variable.
##        x = ""
##        for Item in self.Input:
##            x += Item
##            x += " "
##        return x
##Value1 = MyClass("Red", "Green", "Blue")#all three def will work on value1. but there is nothing for __add__ to do. 
##Value2 = MyClass("Yellow", "Purple", "Cyan")#all three def will work on value2. but there is nothing for __add__ to do.
##Value3 = Value1 + Value2
##print("{0} + {1} = {2}".format(Value1, Value2, Value3))
##print ('this is how we have defined how + should work for objects.')

####importing
##import sys
##for p in sys.path:
##    print (p)#gives list of locations from where files can be imported
##
##sys.path.append('path')#will add another location to this list
##
##import os
##os.chdir('path')#tell python to import from here for now
##print (getcwd())#gives your current source of the file to be imported

####importing class
##import External
##samsr = External.MyClass() #samsr is instance, hence an object that will use default data
##amysr = External.MyClass('Amy', 25) #this object gets custom data
##print (samsr.GetAge())
##samsr.SetAge(35)
##print (amysr.Name)#another way to print value of instance variable
##amysr.SetName('Aimee')
##print (samsr)#it will print since we have defined __str__() for this class
##print (amysr)

####making and using child class
##from External import Animal
##class Chicken(Animal):#tells to inherit from animal thus making chicken a child class
##    def __init__(self, Name='', Age=0):#overides contructor of parent class
##        self.Name = Name
##        self.Age = Age
##        self.Type = 'Chicken'
###since other def are not present we have accepted them as is
##    def SetType(self, Type):
##        print ('Sorry, {0} will always be a {1}'.format (self.Name, self.Type))
##
##    def MakeSound(self):#a new function/feature
##        print ('{0} says Cluck, Cluck!!'.format(self.Name))
##        
##mychick = Chicken ('Sona', 2)
##print (mychick)
##mychick.SetAge(mychick.GetAge() + 1)
##mychick.SetType('Gorilla')
##print (mychick)
##mychick.MakeSound()

##getting data from xml file which has now extended to my project

#importing conversion key from excel book
from openpyxl import load_workbook

wb = load_workbook('Unicode Font - Code Sheet - Values Only.xlsx')
#print (wb.get_sheet_names())

ws_input = wb.get_sheet_by_name ('Input - Values Only')
#print (ws_input)
input_range1 = ws_input ['C3':'S38']
#print (input_range1)
input_list = []
for rows in input_range1:
    for cell in rows:
        input_list.append (cell.value)
input_range2 = ws_input ['C39':'C45']
for rows in input_range2:
    for cell in rows:
        input_list.append (cell.value)
input_list = [w.replace (' @m', '@m') for w in input_list] #good way to replace list's contents. but here need a more efficient way.
#print (input_list)

ws_output = wb.get_sheet_by_name ('Output - Values Only')
#print (ws_output)
output_range1 = ws_output ['C3':'S38']
#print (output_range1)
output_list = []
for rows in output_range1:
    for cell in rows:
        output_list.append (cell.value)
output_range2 = ws_output ['C39':'C45']
for rows in output_range2:
    for cell in rows:
        output_list.append (cell.value)
#print (output_list)

#converts one word at a time
word = "bhagavAn"
def convert (z = word):# the function is skipping the word to convert if it cannot find a match for two consecutive charachters
    z = z.replace("‘","")#inefficient. first check if z has character that needs to be replaced. if yes, then do actual replacement.
    z = z.replace("’","")#inefficient. first check if z has character that needs to be replaced. if yes, then do actual replacement.
    initiate = 0
    terminate = len (z)
    full_output = ''
    switch = False
    while terminate > initiate:
        y = z[initiate:terminate]        
        start = 0        
        if len (y) < 5:
            end = len (y)
        else:
            end = 5
        while end > start:
            x = y[start:end]           
            try:
                part_output = output_list[input_list.index(x)]                
                full_output += part_output
                
                start += len (x)# put the length in variable and use that variable
                initiate += len (x)
            except:#use a specific exception
                end -= 1
                if len (x) == 1:
                    terminate -= 1                   
                    #print (full_output + x)
                    return full_output + x
                    switch = True
                                        
    if switch == False:
        #print (full_output)
        return full_output
    
convert ()

#splits header and footer

sample = 'provAca vinayAddhImAnRuShINAM#foot@ ‘bhagavAn dhImAn’ iti pA.;# vAkyamuttamam'
def convert_to_dev_unicode(sentence = sample):
    if '#' in sentence:#checks if sentence has footers
        list_sentence_splits = sentence.split('#')#sentence splitted into multiple headers and multiple footers in kept in a list
        #print (len(list_sentence_splits))
        sentence_splits_count = 0
        header = ''
        footer_list = []    
        while sentence_splits_count < len(list_sentence_splits):#all headers concaneted and sent to single variable. all footers compiled into a new list
            header += list_sentence_splits[sentence_splits_count]
            if sentence_splits_count + 1 < len(list_sentence_splits):
                footer_list.append(list_sentence_splits[sentence_splits_count + 1])
            sentence_splits_count += 2
        #print (header)
        #print (len(footer_list))
    else:
        header = sentence
        footer_list = []#necessary to avoid exception but inefficient.
        
    #splits each individual header & footer sentence into individual word, converts it and concatenates them together
    #think should make a function out of it
    header_split = header.split(' ')#splitting the single variable into individual words and compiling the pieces in a list.
    converted_header = ''
    for every_header_split in header_split:
        converted_header += convert(every_header_split) + ' '#converting individual word, adding a space and concatenating them together
    print (converted_header.rstrip())

    if len(footer_list) > 0:
        for every_footer in footer_list:
            footer_split = every_footer[6:].split(' ')
            converted_footer = ''
            for every_footer_split in footer_split:
                converted_footer += convert(every_footer_split) + ' '
            print (converted_footer.rstrip())

#imports everything from the xml file    
import xml.etree.ElementTree as ET
import itertools
tree = ET.parse ('caraka.xml')#parses the xml file
samhita = tree.getroot()#gets the root element
#print (samhita.tag)
##print (samhita.text)
print (samhita.items(),'\n')#prints the list of attributes of the elements
for sthana in itertools.islice (samhita, 0, 1):#will loop through 0 to 1 sthana elements and will include all its sub-elements
    #print (sthana.tag)
    for adhyaya in itertools.islice (sthana, 0, 1):
        #print (adhyaya.tag)
        for adhikarana in itertools.islice (adhyaya, 0, 1):
            #print (adhikarana.tag)
            for vyakhya_or_padya_gadya in itertools.islice (adhikarana, 0, 1):
                #print (vyakhya.tag)
                if vyakhya_or_padya_gadya.tag == 'vyakhya':
                    for vya in itertools.islice (vyakhya_or_padya_gadya, 0, 1):
                        #print (vya.tag)
                        for vya_text in vya:
                            print (sthana.items())
                            print (adhyaya.items())
                            print (adhikarana.items())
                            print (vyakhya_or_padya_gadya.items())
                            print (vya.items())
                            print (vya_text.items())
                            convert_to_dev_unicode (vya_text.text)

                elif vyakhya_or_padya_gadya.tag == 'padya_gadya':
                    for pada in vyakhya_or_padya_gadya:
                        print (sthana.items())
                        print (adhyaya.items())
                        print (adhikarana.items())
                        print (vyakhya_or_padya_gadya.items())
                        print (pada.items())
                        convert_to_dev_unicode (pada.text)

#print (samhita[0][0][0][0][0][0].text)

##dic = {}
##for every_object in object_list:
##    count = 0
##    for every_instance in every_object:
##        count += 1
##    dic.update ({every_object.__name__,count})


##import xml.dom.minidom
##
##xml_document = xml.dom.minidom.parse("caraka.xml")
##xml_doc_elements = xml_document.documentElement
##
##sthana = xml_doc_elements.getElementsByTagName ('sthana')
##adhyaya = xml_doc_elements.getElementsByTagName ('adhyaya')
##adhikarana = xml_doc_elements.getElementsByTagName ('adhikarana')
##vyakhya = xml_doc_elements.getElementsByTagName ('vyakhya')
##vya = xml_doc_elements.getElementsByTagName ('vya')
##vya_text = xml_doc_elements.getElementsByTagName ('vya_text')
##padya_gadya = xml_doc_elements.getElementsByTagName('padya_gadya')
##pada = xml_doc_elements.getElementsByTagName ('pada')

##object_list = [sthana, adhyaya, adhikarana, vyakhya, vya, vya_text, padya_gadya, pada] 

##for every_object in object_list:
##    import itertools
##    start = 0 #this will not be printed
##    end = 0
##    count = 1
##    for every_instance in every_object:
##        end += 1
##    print ('Total Count of Element :', end)
##    for every_instance in itertools.islice (every_object, start, 2):
##        print ('Count: ', count)
##        print ('Element Name :',every_instance.tagName)
##        #attribute pair is a touple and items() is a list. Hence we get list of touples
##        for each_touple in every_instance.attributes.items():
##            attrName = each_touple[0]#index of content in touple
##            attrValue = each_touple[1]
##            print ('Attribute :',attrName, ' : ', attrValue)
##        if not every_instance.childNodes[0].data.strip(): #strip method removes the spaces
##            print ('No data\n')
##        else:
##            print ('Element Value :',every_instance.childNodes[0].data,'\n')
##        count += 1

##limit = 0
##import itertools
##for every_pada in pada:
##    limit += 1
##print (limit)

###1st method
##for every_padya_gadya in padya_gadya_tag:
##    pada = every_padya_gadya.getElementsByTagName('pada')[0]
##    print (pada.childNodes[0].data)
##    x += 1
##    if x == limit:
##      break

##for index, every_padya_gadya in zip (range(limit),padya_gadya_tag):
### index += 1 and index = 0 by default. for loop will stop when range(limit) is reached.
##    pada = every_padya_gadya.getElementsByTagName('pada')[0]
##    #this is printing only first pada tag not the consecutive ones. will have to keep a loop here.
##    print (pada.childNodes[0].data)

###using iteration tool function to count and limit it.
##import itertools
##for every_pada in itertools.islice (pada, 0, 10):
##    print (every_pada.childNodes[0].data)
##    print (every_pada.getAttribute('number'))

##import itertools
##for every_sthana in itertools.islice (sthana, 0, 2):
##    print (every_sthana.tagName)
##    for attr in every_sthana.attributes.items():
##        if not attr:
##            print ('No Attributes')
##        else:
##            print ('Attribute - ', attr[0], ' : ', attr[1])
##    if not every_sthana.childNodes[0].data.strip(): #strip method removes the spaces
##        print ('No data\n')
##    else:
##        print ('Element Value :',every_sthana.childNodes[0].data,'\n')
##
##    for every_adhyaya in itertools.islice (adhyaya, 0, 2):
##        print (every_adhyaya.tagName)
##        for attr in every_adhyaya.attributes.items():
##            if not attr:
##                print ('No Attributes')
##            else:
##                print ('Attribute - ', attr[0], ' : ', attr[1])
##        if not every_adhyaya.childNodes[0].data.strip(): #strip method removes the spaces
##            print ('No data\n')
##        else:
##            print ('Element Value :',every_adhyaya.childNodes[0].data,'\n')
##
##        for every_adhikarana in itertools.islice (adhikarana, 0, 2):
##            print (every_adhikarana.tagName)
##            for attr in every_adhikarana.attributes.items():
##                if not attr:
##                    print ('No Attributes')
##                else:
##                    print ('Attribute - ', attr[0], ' : ', attr[1])
##            if not every_adhikarana.childNodes[0].data.strip(): #strip method removes the spaces
##                print ('No data\n')
##            else:
##                print ('Element Value :',every_adhikarana.childNodes[0].data,'\n')
##
##            for every_vyakhya in itertools.islice (vyakhya, 0, 2):
##                print (every_vyakhya.tagName)
##                for attr in every_vyakhya.attributes.items():
##                    if not attr:
##                        print ('No Attributes')
##                    else:
##                        print ('Attribute - ', attr[0], ' : ', attr[1])
##                if not every_vyakhya.childNodes[0].data.strip(): #strip method removes the spaces
##                    print ('No data\n')
##                else:
##                    print ('Element Value :',every_vyakhya.childNodes[0].data,'\n')
##
##                for every_vya in itertools.islice (vya, 0, 2):
##                    print (every_vya.tagName)
##                    for attr in every_vya.attributes.items():
##                        if not attr:
##                            print ('No Attributes')
##                        else:
##                            print ('Attribute - ', attr[0], ' : ', attr[1])
##                    if not every_vya.childNodes[0].data.strip(): #strip method removes the spaces
##                        print ('No data\n')
##                    else:
##                        print ('Element Value :',every_vya.childNodes[0].data,'\n')
##
##                    for every_vya_text in itertools.islice (vya_text, 0, 2):
##                        print (every_vya_text.tagName)
##                        for attr in every_vya_text.attributes.items():
##                            if not attr:
##                                print ('No Attributes')
##                            else:
##                                print ('Attribute - ', attr[0], ' : ', attr[1])
##                        if not every_vya_text.childNodes[0].data.strip(): #strip method removes the spaces
##                            print ('No data\n')
##                        else:
##                            print ('Element Value :',every_vya_text.childNodes[0].data,'\n')
##
##            for every_padya_gadya in itertools.islice (padya_gadya, 0, 2):
##                print (every_padya_gadya.tagName)
##                for attr in every_padya_gadya.attributes.items():
##                    if not attr:
##                        print ('No Attributes')
##                    else:
##                        print ('Attribute - ', attr[0], ' : ', attr[1])
##                if not every_padya_gadya.childNodes[0].data.strip(): #strip method removes the spaces
##                    print ('No data\n')
##                else:
##                    print ('Element Value :',every_padya_gadya.childNodes[0].data,'\n')
##
##                for every_pada in itertools.islice (pada, 0, 2):
##                    print (every_pada.tagName)
##                    for attr in every_pada.attributes.items():
##                        if not attr:
##                            print ('No Attributes')
##                        else:
##                            print ('Attribute - ', attr[0], ' : ', attr[1])
##                    if not every_pada.childNodes[0].data.strip(): #strip method removes the spaces
##                        print ('No data\n')
##                    else:
##                        print ('Element Value :',every_pada.childNodes[0].data,'\n')
