class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("This animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color

    def make_sound(self):
        print("Meow!")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal.name)


# Example usage of the Animal, Dog, Cat, and Zoo classes
dog = Dog("Fido", "Labrador Retriever")
cat = Cat("Whiskers", "Tabby")
zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)

print("Zoo animals:")
zoo.list_animals()

print("Dog's species:", dog.species)
print("Cat's color:", cat.color)

dog.make_sound()
cat.make_sound()
