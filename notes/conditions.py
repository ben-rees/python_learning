# Python uses boolean variables to evaluate conditions. The boolean values True and False are
# returned when an expression is compared or evaluated.

n = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
# Variable assignment is done using an equals operator "=". Comparison between two variables is
# done using the double equals operator "==". The "not equals" operator is marked as "!=".

# Boolean can be made more complex by using the "and" and "or" operators.

name = "Ben"
age = 26
if name == "Ben" and age == 26:
	print("Your name is, Ben and you are also 26 years old")
# or to show off and use string formatting.
if name == "Ben" and age == 26:
	print("Your name is %s, and you are also %d years old" %(name %age))
# Or example
if name == "Ben" or name == "Steve":
	print("Your name is either Ben or Steve")
#Note the 4 space indentations with tab when following an if statement and the colon before.

# The "in" operator could be used to check if a specified object exists within an iterable object
# container, such as a list.

name = "Ben"
if name in ["Ben", "Rick"]:
    print("Your name is either Ben or Rick.")
# Square brackets are a list which the" in" operator is searching through.

# Python uses indentation to define code blocks, instead of brackets. The standard Python
# indentation is 4 spaces, although tabs and any other space size will work, as long as it is
# consistent. Notice that code blocks do not need any termination.

if <statement is="" true="">:
    <do something="">
    ....
    ....
elif <another statement="" is="" true="">: # else if
    <do something="" else="">
    ....
    ....
else:
    <do another="" thing="">
    ....
    ....
</do></do></another></do></statement>
# Practical example of this below

x = 2
if x == 2:
	print("x equals two")
else:
	print("x does not equal to two")
# Else gives an instruction in the event of a false if operator.

# The True statement will also be given if an object is not empty e.g. An empty string or list or
# the number zero


#The "is" operator is different to "==", it doesn't match values of variables but the
# instances themselves

x = [1, 2, 3]
y = {1, 2, 3]
print(x == y) # prints out True
print(x is y) # prints out False
# X and Y's values are the same but are literally different when using "is".

# Using "not" before boolean inverts it

print(not False) # prints out True
print((not False) == (False)) # prints out False
# Comparing "not False" to "False" is essentially comapring "True" to "False"


# Excercise code (completed)

# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
