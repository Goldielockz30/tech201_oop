# Initialisation

# Initialisation -> Relates to setting a particular data for an instance of a class
# to make an object more specific

# Instantiation -> Is the creation of an instance of an object
class Dog:

    def __init__(self, name, colour): # do this when we initialise the class
        self.animal_kind = "canine" # this is hardcoded, we put this line inside the initialisation block, we cant change it because it is protected
        self.name = name # this is how we store the date
        self.colour = colour
        self.bark()

    def bark(self): # this is a method which is a function within a class,
        return "woof"

fido = Dog("Fido", "Brown") # these are the objects and we use the class to make the objects
lassie = Dog("Lassie", "Brown")

print(fido.name)
print(fido.colour)

# to specify things when we create an object we use
# __init__
# Initialising a class with variables is good practice. It is possible to set variables