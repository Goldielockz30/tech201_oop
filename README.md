# tech201_oop
tech201_oop

# Object-Oriented Programming (OOP)

# Everything in OOP is an object and objects are modeled against real world objects.

# Classes are the templates we use to create objects
# Classes are a way of bringing both the data and functionality of our code together


# we are making templates when we create a class
# Create a class
# To name it use snake case eg. WonderDog # start with capital

class Dog:

    animal_kind = "canine" # class variable # what is the scope of this variable?
    # lets give it a behaviour

    def bark(self): # class method, even though this looks like a function but because it is inside the scope of the class it then becomes a method
        # print(self.animal_kind) # we go into the class to access the variable
        return "woof"

# self - "I'm referring to the current class.
# def bark(self): # this refers to the class dog
# look at this object for this animal variable and look into the dog class

#print(Dog.animal_kind) # access the object animal_kind

 # print(Dog.animal_kind()) # this does not work #ERROr

 # Instantiation of a class, # Creating or making an object from a class

fido = Dog()
lassie = Dog()


print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
print(lassie.bark())

# fido.animal_kind = "Big Dog" # this will change the variable for just fido object but lassie will stay as canine

print(fido.animal_kind)
print(lassie.animal_kind)

# lassie.animal_kind = "Turtle" # lassie will become turtle because we have overwritten the template
Dog.animal_kind = "Dolphin" # this has overwritten the template so will change the variable for both objects
# this is an Instance Variable rather than a Class Variable, Dog.animal_kind = "Dolphin"

print(fido.animal_kind)
print(lassie.animal_kind)

# The Dog's can still access their method
print(fido.bark())
print(lassie.bark())

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


# Methods

class MethodExamples:

    # this_can_be_accessed_easily = "Hi, I am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!" # this is for a classs variable , for a method we would use two underscores
    # we have protected it by putting it into this initialise block
    # def get_this_can_be_accessed_easily(self):
    #     return self.this_can_be_accessed_easily
    #
    # def get_this_can_be_accessed_easily(self, value_to_be_set):
    #     return self.this_can_be_accessed_easily = value_to_be_set

# x = MethodExamples()
#
# print(x.this_can_be_accessed_easily)
# x.this_can_be_accessed_easily = "I have been changed!"
# print(x.this_can_be_accessed_easily)  # we don't want to overwrite everything



# Public and private


x = MethodExamples()

print(x.get_this_can_be_accessed_easily()) # for methods we use double underscore
x.set_this_can_be_accessed_easily("I have been changed!")
print(x.get_this_can_be_accessed_easily())  # we don't want to overwrite everything


# __name__ and __main_

# to use these we need two seperate files

# in this case name = main

#


# mod 1

# print(__name__)

# print("This is mod1's name -> " + __name__)

def main():
    # pass     # a key word statement which means none/null its just a placeholder
    print("This is mod1's name -> " + __name__)
if __name__ == "__main__": # the name cannot be imported it only runs this within the base file, it allows us to know when code is being ran by the current file or another file
    main()
    # to understand where the code is being run from and determine where you would want it to run
 # this helps you to have more control over what gets executed and what doesnt

# mod 2

print("This is mod2's name -> " + __name__)
