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

