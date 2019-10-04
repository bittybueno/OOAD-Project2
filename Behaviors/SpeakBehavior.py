import abc
from abc import ABC, abstractmethod
import random

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
        