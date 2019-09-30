import abc
from abc import ABC, abstractmethod
import random

class Animal(ABC): 
    
    def __init__(self, name):
        self.name = name
        self.family = None
        self.species = None
        self.roamBehavior = None
        self.speakBehavior = None
        self.eatBehavior = None

     
    def getAnimalSpecies(self):
        return self.species

    def getAnimalFamily(self):
        return self.family

    def getAnimalName(self):
        return self.name
  
    def SetSpeakBehavior(self, sb):
        self.speakBehavior = sb
    
    def SetEatBehavior(self, eb):
        self.eatBehavior = eb

    def SetRoamBehavior(self, rb):
        self.roamBehavior = rb
        
        
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
    
      
    def printAnimal(self):
        print("This animal is a(n) " + self.getAnimalSpecies() + " of the " + self.getAnimalFamily()
                + " family, and its name is " + self.getAnimalName())


############################        
class RoamBehavior(object):
    def roam(self):
        pass

class ZoomiesRoam(RoamBehavior):
    def roam(self):
        print("ZOOOOOMIES. ZOOOOOOOOOM.")

class DoggyRoam(RoamBehavior):
    def roam(self):
      print("*Runs*")

class StompingRoam(RoamBehavior):
    def roam(self):
       print("STOMP. STOMP. STOMP")

############################
class EatBehavior(object):
    def eat(self):
        pass

class Herbivore(EatBehavior):
    def eat(self):
        print("Cronching on some Hay and fruit")

class Carne(EatBehavior):
    def eat(self):
       print("Eating some meats!")

############################
class SpeakBehavior(object):
    def makeNoise(self):
        pass

class RoarSound(SpeakBehavior):
    def makeNoise(self):
        print("ROARRRRR")
        
class RoarSound2(SpeakBehavior):
    def makeNoise(self):
        print("Theyyyyy're great!")

class MeowSound(SpeakBehavior):
    def makeNoise(self):
      list = ["meow", "prr", "rreeeooow", "hsssst"]
      noise = random.choice(list)
      print(noise)

class HuffSound(SpeakBehavior):
    def makeNoise(self):
       print("Hufffff, *kicks dirt up with horn*")
        
class HuffSound2(SpeakBehavior):
    def makeNoise(self):
       print("ppprrrrrrrrrph")
        
class HuffSound3(SpeakBehavior):
    def makeNoise(self):
       print("hungry hungry hippo!")        

class BarkSound(SpeakBehavior):
    def makeNoise(self):
        print("AWOOOOOOOOOOOOOOOOOO *in a badass wild tone*")
        
class BarkSound2(SpeakBehavior):
    def makeNoise(self):
        print("ruff ruff!!")

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

################################################
##Creating Felines##
Cathy = Cat("Cathy")
Cory = Cat("Cory")
Clyde = Cat("Clyde")

Tony = Tiger("Tony")
Tammy = Tiger("Tammy")

Leo = Lion("Leo")
Lauren = Lion("Lauren")
##Creating Pachyderms##
Ron = Rhino("Ron")
Rhonda = Rhino("Rhonda")

Elle = Elephant("Elle")
Ernie = Elephant("Ernie")

Henry = Hippo("Henry")
Hannah = Hippo("Hannah")
##Creating Canines##
Wally = Wolf("Wally")
Wonda = Wolf("Wonda")

Doug = Dog("Doug")
Daffy = Dog("Daffy")

##Appending animals to list##
animalList = []
animalList.append(Cathy)
animalList.append(Cory)
animalList.append(Clyde)
animalList.append(Tony)
animalList.append(Tammy)
animalList.append(Leo)
animalList.append(Lauren)
animalList.append(Ron)
animalList.append(Rhonda)
animalList.append(Elle)
animalList.append(Ernie)
animalList.append(Henry)
animalList.append(Hannah)
animalList.append(Wally)
animalList.append(Wonda)
animalList.append(Doug)
animalList.append(Daffy)



  
#Global methods to command Animals 
def wakeUp():
  for i in range(len(animalList)):
    (animalList[i].wake())
    print()
    
def rollCall():
  for i in range(len(animalList)):
    print(animalList[i].name, " the ", animalList[i].family, " goes:")
    (animalList[i].PerformSpeakBehavior())
    print()
def feed():
  for i in range(len(animalList)):
    print(animalList[i].name, " the ", animalList[i].family, " is ")
    (animalList[i].PerformEatBehavior())
    print()
def exercise():
  for i in range(len(animalList)):
    print(animalList[i].name, " the ", animalList[i].family, " exercising:")
    (animalList[i].PerformRoamBehavior())
    print()
def goToSleep():
  for i in range(len(animalList)):
    (animalList[i].sleep())
    print()
    
############### ZooKeeper & ZooAnnouncer Class ##################

class Subscriber: 
    def __init__(self, name):
        self.name = name
        
    def update(self, message):
        print('{} gets the "{}" cue from the ZooKeeper'.format(self.name, message))
        print('{} says, "Time to {} the animals!"'.format(self.name, message))

        
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
        
    def register(self, who):
        self.subscribers.add(who)
        
    def unregister(self, who):
        self.subscribers.discard(who)
        
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)
            
    #for creating animals
    def putToBed(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Bed Time!'\n")
      goToSleep()
    
    def wakeEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Rise and shine!'\n")
      wakeUp()
   
    def feedEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Lunch Time!'\n")
      feed()
    
    def exerciseEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()  
      print("ZooKeeper says, 'Let's get moving!'\n")
      exercise()
      
    def callEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Roll Call!'\n")      
      rollCall()

############### Commands ####################


zooKeeper = Publisher()

ZooAnnouncer = Subscriber('ZooAnnouncer')
zooKeeper.register(ZooAnnouncer)

zooKeeper.wakeEm("wake up")
zooKeeper.callEm("rollcall")
zooKeeper.feedEm("feed")
zooKeeper.exerciseEm("exercise")
zooKeeper.putToBed("tuck in")




