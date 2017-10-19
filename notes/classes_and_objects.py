# Objects are an encapsulation of variables and functions and get this from classes.
# Classes are like a folder for variables and functions to be grouped in and act as a
# template to creat your objects with.

# A very basic class below.

class MyClass:
	variable = "string"

	def function(self):
		print("This is a class")
# The "self" parameter isn't explained yet. Ammend this note later. Maybe object name takes it place when assigned later?

# Now to assign a class to an objectclass MyClass:

class MyClass:
        variable = "string"

        def function(self):
                print("This is a class")

object_name = MyClass()
# Now "object_name" holds an object(version) of "MyClass".

# To access a variable within an object

class MyClass:
        variable = "string"

        def function(self):
                print("This is a class")

object_name = MyClass()

object_name.variable
# Object's name.Variable name.

print(object_name.variable)
# This would print "string" in this scenario

# You can create multiple objects based on the same class and each object will have an
# independant copy of the variables. Changing the values within one will not affect the others.

class MyClass:
    variable = "string"
    def function(self):
        print("This is a message.")

objectx = MyClass()
objecty = MyClass()

objecty.variable = "something else"

# Then pring out both values
print(objectx.variable)
print(objecty.variable)
# x would still say "string" whereas y now says "something else"

# Accessing functions works much the same way.
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message.")

object = MyClass()

object.function()
# This would trigger the print() function


# Exercise. We have a class defined for vehicles. Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue
# van named Jump worth $10,000.00 (Solved).


# define the Vehicle class

class Vehicle:
    name = ""
    kind = "car"
    colour = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.colour, self.kind, self.value)
        return desc_str

# your code goes here

car1 = Vehicle()
car2 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.colour = "red"
car1.value = 60000.00
car2.name = "Jump"
car2.kind = "van"
car2.colour = "blue" 
car2.value = 10000.00

# test code

print(car1.description())
print(car2.description())
# Note how a class is specified before calling the function.
