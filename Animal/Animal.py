
Animal.ipynb
Animal.ipynb_
Dog
import abc
from abc import ABC, abstractmethod
import random
​
class Animal(ABC): 
    
    def __init__(self, name):
        self.name = name
        self.family = None
        self.species = None
        self.roamBehavior = None
        self.speakBehavior = None
        self.eatBehavior = None
​
      
​
        
    def getAnimalSpecies(self):
        return self.species
​
    def getAnimalFamily(self):
        return self.family
​
    def getAnimalName(self):
        return self.name
  
    def SetSpeakBehavior(self, sb):
        self.speakBehavior = sb
    
    def SetEatBehavior(self, eb):
        self.eatBehavior = eb
​
    def SetRoamBehavior(self, rb):
        self.roamBehavior = rb
    
    def PerformSpeakBehavior(self):
        self.speakBehavior.makeNoise()
​
    def PerformEatBehavior(self):
        self.eatBehavior.eat()
​
    def PerformRoamBehavior(self):
        self.roamBehavior.roam()
        
    def PerformSleepBehavior(self):
        self.sleepBehavior.sleep()
    
    def sleep(self):
      print(self.getAnimalName(), "the", self.getAnimalFamily(), "is asleep!\n *snores*")
​
    def printAnimal(self):
        print("This animal is a(n) " + self.getAnimalSpecies() + " of the " + self.getAnimalFamily()
                + " family, and its name is " + self.getAnimalName())
​
​
        
class RoamBehavior(object):
    def roam(self):
        raise NotImplementedError
​
class ZoomiesRoam(RoamBehavior):
    def roam(self):
        print("ZOOOOOMIES. ZOOOOOOOOOM.")
​
class DoggyRoam(RoamBehavior):
    def roam(self):
      print("*Runs*")
​
class StompingRoam(RoamBehavior):
    def roam(self):
       print("STOMP. STOMP. STOMP")
​
​
class EatBehavior(object):
    def eat(self):
        raise NotImplementedError
​
class Herbivore(EatBehavior):
    def eat(self):
        print("Cronching on some Hay and fruit")
​
class Carne(EatBehavior):
    def eat(self):
       print("Eating some meats!")
​
​
class SpeakBehavior(object):
    def makeNoise(self):
        raise NotImplementedError
​
class RoarSound(SpeakBehavior):
    def makeNoise(self):
        print("ROARRRRR")
​
class MeowSound(SpeakBehavior):
    def makeNoise(self):
      list = ["meow", "prr", "rreeeooow", "hsssst"]
      noise = random.choice(list)
      print(noise)
​
class HuffSound(SpeakBehavior):
    def makeNoise(self):
       print("Hufffff, *kicks dirt up with horn*")
​
class BarkSound(SpeakBehavior):
    def makeNoise(self):
        print("AWOOOOOOOOOOOOOOOOOO *in a badass wild tone*")
​
​
​
################################################
class Feline(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Feline"
        self.roamBehavior = ZoomiesRoam()
        self.eatBehavior = Carne()
​
class Cat(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Cat"
        
class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = RoarSound()
        self.family = "Tiger"
        
class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = RoarSound()
        self.family = "Lion"        
################################################
class Pachyderm(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Pachyderm"
        self.roamBehavior = StompingRoam()
        self.eatBehavior = Herbivore()
​
class Rhino(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Rhino"
        
class Elephant(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Elephant"
        
class Hippo(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Hippo"
################################################
class Canine(Animal):
    def __init__(self,name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Canine"
        self.roamBehavior = DoggyRoam()
        self.eatBehavior = Carne()
​
class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Wolf"
        
class Dog(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Dog"        
​
################################################
cathy = Cat("Cathy")
cathy.PerformSpeakBehavior()
cathy.PerformEatBehavior()
cathy.PerformRoamBehavior()
cathy.PerformSpeakBehavior()
cathy.sleep()
cathy.printAnimal()

