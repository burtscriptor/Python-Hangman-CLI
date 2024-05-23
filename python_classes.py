# python is more OOP then JS 
# classes are moulds for objects (OOP), the constructor in JS is the equilavent
# encapsulation - bundle related methods and properties like colour name size 4wd AC of a car
# everything in python/JS is an object even strings and numbers, ie array methods, string methods
# double underscore methods __add__, 
#__init__ used for classes

class Dog():
    def __init__(self, name, age=0): # self like this in JS, default age of 0 i case someone for gets age, 
        self.name = name
        self.age = age

    def bark(self): # passing in self to this method in the dog class, means we can use self.name and have access to the name in the method
        print(f'{self.name} says woof!')

    def __str__(self, name,age):
        return f'Dog named {self.name} is {self.age} years old.'

spot = Dog('Jarred', 5) # spot becomes the instance of that class
lassie = Dog('Lassie')
print(spot.name, spot.age) # we use dot notation of instances of classes


