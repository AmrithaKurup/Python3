class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'


tom = Dog('Tom')
kitty = Cat('kitty')

# We can use polymorphism in different ways
# The first method is using for loop
'''
for pet in [tom, kitty]:
    print(pet.name)
    print(pet.speak())
'''
# The second method is using functions


def pet_speak(pet):
    print(pet.speak())


pet_speak(tom)
pet_speak(kitty)

# The most common method is to use abstract classes
