import abc
from abc import ABC, abstractmethod
import random

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
