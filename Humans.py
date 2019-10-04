import abc
from abc import ABC, abstractmethod
import random

from Animals import *

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


if __name__== "__main__":

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

  zooKeeper = Keeper()

  ZooAnnouncer = Announcer('ZooAnnouncer')
  zooKeeper.register(ZooAnnouncer)

  zooKeeper.wakeEm("wake up")
  zooKeeper.callEm("rollcall")
  zooKeeper.feedEm("feed")
  zooKeeper.exerciseEm("exercise")
  zooKeeper.putToBed("tuck in")

  zooKeeper.unregister(ZooAnnouncer)