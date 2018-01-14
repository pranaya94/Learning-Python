class Animal:
	_name = None
	_height = 0
	_sound = 0 #_ is trying to indicate to keep private, not actually private though

	def __init__(self,myname,myheight,mysound):
		self._name = myname
		self._height = myheight
		self._sound = mysound

	def set_name(self, myname):
		self._name = myname

	def set_height(self,myheight):
		self._height = myheight

	def set_sound(self,mysound):	
		self._sound = mysound
	
	def get_type(self):
		print("Animal")

	def get_name(self):
		return self._name

	def get_height(self):
		return self._height

	def get_sound(self):
		return self._sound

	def get_type(self):
		print("Animal")

	def display_info(self):
		return ("{} is {} cm tall and sounds like {}".format(self._name,self._height,self._sound))

cat = Animal('Whiskers',30,'meow')		
print(cat.get_name())
print(cat.display_info())

# __member is private (name of class is magled to it is _Animal__member)
# _member is not
#inheritence
class Dog(Animal):
	__owner = ""

	def __init__(self,name,height,sound,owner):
		self.__owner  = owner
		super(Dog,self).__init__(name,height,sound)

	def get_type(self):
		print("Dog")

	def set_owner(self,owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def display_info(self):		
		return("{} is {} cm tall and sounds like {} and {} is the owner".format(self._name,self._height,self._sound,self.__owner))

	def multiple_sounds(self, n_of_barks = None):
		if n_of_barks == None:
			print("I'm silent")
		else:
			print(self.get_sound() * n_of_barks)

dog = Dog('Pluto',20,'Bow Wow ','Sam')
print(dog.display_info())
dog.multiple_sounds(2)
dog.multiple_sounds(2)

#polymorphism
class AnimalTesting:
	def get_type(self,ani):
		ani.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(dog)

print(dog._Dog__owner)

# when you give __ the name of class gets appended to the name of member