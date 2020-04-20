class Animal ():
	species = 'dog'
	#species is class object attribute available by default for every instance of this object
	#we assign the argument to 
	
	def __init__(self,mybreed,another_attribute):#mybreed will be the argument that user will give and system will take in via this parameter
		self.my_breed = mybreed#system assigns the user provided argument to self.my_breed attribute
		self.my_name = another_attribute #attribute name can be different from the parameter name. Conventionally, they all are kept same.

#def __init__ is called everytime an instance is created.
#The parameters passed to __init__ are used to define attributes of the instance
#self means name of the class

	def bark (self,number):#methods are functions within a class. the word self makes it a method.
		print ('My name is {}, species is {} and number is {}'.format(self.my_name,self.species,number))

##AFTER RUNNING CODE
		
##my_instance = Animal ('Huskie','Aditya')
###huskie becomes value of attribute of my_dog


##my_instance.my_breed #will give
##Huskie
		
##my_instance.bark(2)#will give
##My name is Aditya, species is mammal and number is 1
