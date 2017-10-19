# Lists contain variables. Example of how to build a list below.

list = []
# This creates an empty list due to nothing being in the square brackets.

list.append(1)
list.append(2)
list.append(3)
# This adds to the created list.

#Items in the list begin at zero. To print the first item (1 in this case) use the following.

print(list[0])
# Note the use of square brackets

# To print a list use the following

for x in list:
	print(x)
# Not really sure about the x bit. Just go with it. Also note the 4 space indent below the for
# command.This is important and can be easily done with tab

# This does work with strings (words) too.

words = ["random", "example"]
# Remember the " " to declare a string

# You can add to and recall the same way

words.append("more")
print(words[1])
# This would add "more" to the list and then print the word example. Remember the list starts at 0

