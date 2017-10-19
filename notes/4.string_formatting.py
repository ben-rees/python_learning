# The % operator is used to format variables enclosed in brackets (tuples).
# This takes the form of a bracket, a text string of your choosing, % followed by a specifier.
# Some basic specifiers;

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of
# the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "Ben"
print("Hello, %s!" % name)
# This prints "Hello, Ben!". Note how % name is there to bring the string in

# %s can be used on integers(numbers) too as they have a string value

list = [1, 2, 3]
print("Some numbers: %s" % list)
# This prints "Some numbers: 1, 2, 3"

# To use 2 or more specifiers you need to use brackets (tuples).

name = "Ben"
age = 26
print("%s is %d years old." % (name, age))
# This prints "Ben is 26 years old. Note the double bracket at the end to close out print and the
# specifiers and %d which can be used for integers

# More in depth example.

data = ("Ben", "Rees", 53.44)
format_string = "Hello %s %s. Your current balance is £%s."
print(format_string % data)
# This blows my mind a little. The strings seem to be called up in order. An alternative way of
# achieving this is

data = ("John", "Doe", 53.44)
print("Hello %s %s. Your balance is $%.2f" % data)
# Rather than adding my own strings into a new variable I just entered them all within the print
# function. I used a 2 decimal floating number specifier for the balance because why not.
