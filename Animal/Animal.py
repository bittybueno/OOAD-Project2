#!/usr/bin/env python3
import abc
from abc import ABC, abstractmethod
import random

#Abstract Animals class with attributes of the behaviors and characteristics of an animal
    
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

############## INTERFACES ##############

############# Using a RoamBehavior Interface to customize the behavior ###############        
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

########### Using an EatBehavior Interface to customize the behavior #################
class EatBehavior(object):
    def eat(self):
        pass

class Herbivore(EatBehavior):
    def eat(self):
        print("Cronching on some Hay and fruit")

class Carne(EatBehavior):
    def eat(self):
       print("Eating some meats!")

############# Using a SpeakBehavior Interface to customize the behavior ###############
class SpeakBehavior(object):
    def makeNoise(self):
        pass
#to have a behavior defined on each level of inheritance, the speak behavior interface and implementations
#is designed to be defined per animal type class (Lion, Tiger, Cat, Rhino, Elephant, Hippo, Wolf and Dog classes)
class RoarSound(SpeakBehavior):
    def makeNoise(self):
        print("ROARRRRR")
        
class RoarSound2(SpeakBehavior):
    def makeNoise(self):
        print("Theyyyyy're great!")

class MeowSound(SpeakBehavior): 
#importing random allows for us to have any value in the array of choices of cat responses to be selected for the cat rollcall()
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

################## Creating the Feline Family ##############################
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

################################################

#Because there are so many animals in the zoo, an array of type Animal is created
#so the zookeeper can just call the tasks on the array rather than each animal individually

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

    
############### Subscriber & Publisher Abstract Classes ##################

#A subscriber recieves a message from the publisher
class Sub(ABC): 
    def __init__(self, name):
        self.name = name
        
    def update(self, message):
        pass


   
#A publisher can register and unregister subscribers and send them messages
class Publisher(ABC):
    def __init__(self):
        self.subscribers = set()
        
    def register(self, who):
        self.subscribers.add(who)
        
    def unregister(self, who):
        self.subscribers.discard(who)
        
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


################# Announcer & Keeper Subclasses ##################

#the Announcer subclass extends the Subscriber class so that when it recieves a message
#from the Publisher it will acknowlege the cue was recieved and then repeat the cue to 
#the zoo
class Announcer(Sub):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name  

    def update(self, message):
        print('{} gets the "{}" cue from the ZooKeeper'.format(self.name, message))
        print('{} says, "Time to {} the animals!"'.format(self.name, message)) 

#the Keeper subclass extends the Publisher class so that it can register, unregister and also
#send messaged to any subscribers. The Keeper class also holds methods to command the animals
#to wake up, excerise, talk, eat and sleep.
class Keeper(Publisher):
   
        
    #ZooKeepers Methods for Animals
    def putToBed(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Bed Time!'\n")
      for i in range(len(animalList)):
        (animalList[i].sleep())
        print()
    
    def wakeEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Rise and shine!'\n")
      for i in range(len(animalList)):
        (animalList[i].wake())
        print()
   
    def feedEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Lunch Time!'\n")
      for i in range(len(animalList)):
        print(animalList[i].name, " the ", animalList[i].family, " is ")
        (animalList[i].PerformEatBehavior())
        print()
    
    def exerciseEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()  
      print("ZooKeeper says, 'Let's get moving!'\n")
      for i in range(len(animalList)):
        print(animalList[i].name, " the ", animalList[i].family, " exercising:")
        (animalList[i].PerformRoamBehavior())
        print()
      
    def callEm(self, message):
      for subscriber in self.subscribers:
        subscriber.update(message)
      print()
      print("ZooKeeper says, 'Roll Call!'\n")      
      for i in range(len(animalList)):
        print(animalList[i].name, " the ", animalList[i].family, " goes:")
        (animalList[i].PerformSpeakBehavior())
        print()

############### Commands ####################


zooKeeper = Keeper()

ZooAnnouncer = Announcer('ZooAnnouncer')
zooKeeper.register(ZooAnnouncer)

zooKeeper.wakeEm("wake up")
zooKeeper.callEm("rollcall")
zooKeeper.feedEm("feed")
zooKeeper.exerciseEm("exercise")
zooKeeper.putToBed("tuck in")

zooKeeper.unregister(ZooAnnouncer)



