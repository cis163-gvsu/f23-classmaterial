#from abc import ABC, ABCMeta, abstractmethod
import abc
import matplotlib.pyplot as plt

class Animal(abc.ABC):
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(f"Animal's name is {self.name}")

    
    @abc.abstractmethod
    def eat(self, amount):
        pass
    

class Dog(Animal):
    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)

    def make_noise(self):
        print('woof woof')

    # this is necessary for Dog to not be abstract
    def eat(self, amount):
        self.weight += amount


'''
# this is invalid
a = Animal('bob')
a.print_name()
'''

d = Dog('Chewie', 30)
d.print_name()
d.make_noise()
