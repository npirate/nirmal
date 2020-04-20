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

##using class in applications. Class created here. will be used somewhere else.
class MyClass:
    def __init__(self, Name="Sam", Age=32):#sets defaults to be used
        self.Name = Name
        self.Age = Age
    def GetName(self):
        return self.Name #GetName will receive name from input
    def SetName(self, Name):
        self.Name = Name #will set the name. if error while input self.Name will use default value.
    def GetAge(self):
        return self.Age
    def SetAge(self, Age):
        self.Age = Age
    def __str__(self):#converts object to string.
        return "{0} is aged {1}.".format(self.Name,self.Age)

class Animal:
    def __init__(self, Name="", Age=0, Type=""):
        self.Name = Name
        self.Age = Age
        self.Type = Type
    def GetName(self):
        return self.Name
    def SetName(self, Name):
        self.Name = Name
    def GetAge(self):
        return self.Age
    def SetAge(self, Age):
        self.Age = Age
    def GetType(self):
        return self.Type
    def SetType(self, Type):
        self.Type = Type
    def __str__(self):
        return "{0} is a {1} aged {2}".format(self.Name,self.Type,self.Age)    

##creating content for storage
class FormatData:
    def __init__(self, Name='', Age=0, Married=False):
        self.Name = Name
        self.Age = Age
        self.Married = Married

    def __str__(self):
        output - "'{0}', {1}, {2}".format(
            self.Name,
            self.Age,
            self.Married)
        return output
