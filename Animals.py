import abc
from abc import ABC, abstractmethod
import random

from Behaviors.EatBehavior import *
from Behaviors.SpeakBehavior import *
from Behaviors.RoamBehavior import *



#Abstract Animals class with attributes of the behaviors and characteristics of an animal
class Animal(object):  
    def __init__(self, name):
        self.name = name
        self.family = None
        self.species = None
        self.roamBehavior = None
        self.speakBehavior = None
        self.eatBehavior = None

   #getter methods  
    def getAnimalSpecies(self):
        return self.species

    def getAnimalFamily(self):
        return self.family

    def getAnimalName(self):
        return self.name
    #setter methods
    def SetSpeakBehavior(self, sb):
        self.speakBehavior = sb
    
    def SetEatBehavior(self, eb):
        self.eatBehavior = eb

    def SetRoamBehavior(self, rb):
        self.roamBehavior = rb
        
    #commands to speak, eat, roam, wake, sleep    
    def PerformSpeakBehavior(self):
        self.speakBehavior.makeNoise()

    def PerformEatBehavior(self):
        self.eatBehavior.eat()     

    def PerformRoamBehavior(self):
        self.roamBehavior.roam()

    def wake(self):
      print(self.getAnimalName(), "the", self.getAnimalFamily(), "is awake!")
            
    def sleep(self):
      print(self.getAnimalName(), "the", self.getAnimalFamily(), "is asleep!\n *snores*")
    
     
    #method to return the description of an animal 
    def printAnimal(self):
        print("This animal is a(n) " + self.getAnimalSpecies() + " of the " + self.getAnimalFamily()
                + " family, and its name is " + self.getAnimalName())

################# Creating the Feline Family ##############################
class Feline(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Feline"
        self.roamBehavior = ZoomiesRoam()
        self.eatBehavior = Carne()

## inheriting from Feline which inherits from ABC Animal ##
class Cat(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Cat"
        
class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = RoarSound2()
        self.family = "Tiger"
        
class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = RoarSound()
        self.family = "Lion"        




################### Creating the Pachyderm Family #############################
class Pachyderm(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Pachyderm"
        self.roamBehavior = StompingRoam()
        self.eatBehavior = Herbivore()

## inheriting from Pachyderm which inherits from ABC Animal ##
class Rhino(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Rhino"
        
class Elephant(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound2()
        self.family = "Elephant"
        
class Hippo(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound3()
        self.family = "Hippo"
#################### Creating the Canine Family ############################
class Canine(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Canine"
        self.roamBehavior = DoggyRoam()
        self.eatBehavior = Carne()

## inheriting from Canine which inherits from ABC Animal ##
class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Wolf"
        
class Dog(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = BarkSound2()
        self.family = "Dog"        
