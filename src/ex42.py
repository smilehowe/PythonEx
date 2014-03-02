#coding:utf-8

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object, Dog继承了Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## has-a
        self.name = name

## Cat is-a object, Cat继承了Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## has-a
        self.name = name
        
## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ##??
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Fish is-a object
class Fish(object):
    pass

## Salmon is-a object, Salmon继承了Fish
class Salmon(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")    

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

