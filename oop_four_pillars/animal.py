# This is our base class

# Abstraction

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self): # method
        print("One breath in and one breath out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and Upwards")

cat = Animal()
# cat.breathe() # abstracting the breathe method


