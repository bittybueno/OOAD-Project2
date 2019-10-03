import abc


class Animal(object):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
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

    def printAnimal(self):
        print("This animal is a(n) " + self.getAnimalSpecies() + " of the " + self.getAnimalFamily()
              + " family, and its name is " + self.getAnimalName())


class RoamBehavior(object):
    def roam(self):
        raise NotImplementedError


class ZoomiesRoam(RoamBehavior):
    def roam(self):
        print("ZOOOOOMIES. ZOOOOOOOOOM.")


class StompingRoam(RoamBehavior):
    def roam(self):
        print("STOMP. STOMP. STOMP")


class EatBehavior(object):
    def eat(self):
        raise NotImplementedError


class Herbivore(EatBehavior):
    def eat(self):
        print("Cronching on some Hay and fruit")


class Carne(EatBehavior):
    def eat(self):
        print("Eating some meats!")


class SpeakBehavior(object):
    def makeNoise(self):
        raise NotImplementedError


class RoarSound(SpeakBehavior):
    def makeNoise(self):
        print("ROARRRRR")


class MeowSound(SpeakBehavior):
    def makeNoise(self):
        print("meow")


class HuffSound(SpeakBehavior):
    def makeNoise(self):
        print("Hufffff, *kicks dirt up with horn*")


class BarkSound(SpeakBehavior):
    def makeNoise(self):
        print("AWOOOOOOOOOOOOOOOOOO *in a badass wild tone*")


class Feline(Animal):
    def __init__(self, name):
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


class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Lion"


class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Tiger"


class Canine(Animal):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Canine"
        self.roamBehavior = ZoomiesRoam()
        self.eatBehavior = Carne()


class Dog(Canine):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Dog"


class Wolf(Canine):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Wolf"


class Pachyderm(Animal):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Pachyderm"
        self.roamBehavior = StompingRoam()
        self.eatBehavior = Herbivore()


class Hippo(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Hippo"


class Elephant(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Elephant"


class Rhino(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Rhino"


class ZooKeeper():
    animalArray = [Hippo("Harry"), Hippo("Harvy"), Rhino("Roger"), Rhino("Ronny"), Elephant("Earl"), Elephant("Edgar"), Dog("Daryl"),
                   Dog("Dayna"), Wolf("Wesley"), Wolf("Wyatt"), Lion("Larry"), Lion("Linda"), Tiger("Tony"), Tiger("Terri"), Cat("Cathy"), Cat("Chris")]
