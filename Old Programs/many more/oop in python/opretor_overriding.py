class Animal:
	def speak(self):
		raise NotImplementedError("method hovig g joye...")


class Dog(Animal):

    def speak(self):
        return "woof"


class Cat(Animal):
    

    def ok(self):
        return True



animals = Dog()
animals2= Cat()



print(animals.speak())
print(animals2.ok())


