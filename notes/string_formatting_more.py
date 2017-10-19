twoThirds= 2/3
# Setting a variable as two thirds

print("2 divided by three is about {}" .format(twoThirds))
# Curly braces allow for information to be inserted. This is done with the
# .format argument. Seems similar to the other way which is
# ("%s" %variable name)

print("or with fewer decimal points: {: .2f}" .format(twoThirds))
# Here the curly braces contain formtting information. In this case it's
# formatting as a float and I've specified two decimal places with .2
# before the float (f) argument

randomString = "more"
print("you can print {0} than one variable with .format. {1} is an example."
      .format(randomString,"Here"))
# An example of using .format to insert more than one variable. Unlike the %
# method it appears to have a way of allowing the user to specify what they want
# to be added and where. I add randomString and the word "Here" to the .format
# argument and call upon their postion as if they were a list only I'm using
# {} isntead of []. Also works with functions that return a string
# (e.g. math.pi)

