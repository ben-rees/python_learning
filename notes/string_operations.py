# This bit is a little dry and seems pointless for now. Maybe it'll prove useful later?

# There is more things you can do with strings other than printing them.

string = "Hello World!"
print(len(string))
# This will print 12 because "Hello World!" is 12 characters long including spaces and punctuation.

print(string.index("o"))
# This prints a 4 because the location of the first occurrence of the letter "o" is 4 characters
# away from the first character. There are actually two o's in the phrase but this method only
# recognises the first.
# This didn't print 5 because Python starts things at 0 instead of 1. So the index of "o" is 4.

string = "Hello world!"
print(string.count("l"))
# This counts the number of l's in the string. So three in this case

string = "Hello world!"
print(string[3:7])
# This prints a slice of the string ("lo w" in this case), starting at index 3, and ending at index
# 6. Most languages  will end one digit before specified (6 instead of 7 in this case), its "makes
# doing maths inside the brackets easier". Just accept this is how it is.
# If you leave the left side of the colon blank then it will go from beginning to specified end.
# Leaving the right side blank will go from specified start to the end of the string.
# You can use negative numbers too.

string = "Hello world!"
print(string[-7:-2])
# This would start 7 characters from the end and finish two characters from the end (remember
# the end character quirk). The result would be ( worl). Note the space it counted before the text.

string = "Hello world!"
print(string[0:12:2])
# This prints the characters of string from 0 to 12 skipping one character. This is extended slice
# syntax. The general form is [start:stop:step]. Increments of two in this case.
# The result of this is "Hlowrd". It skipped e, then l, then space, then o, then l and finally !.
# Every other character. A value of 3 would be every 2 characters so the result would be Hlwl.
# Skipping el, then o and space, then or, and finally d!. Can't think of a single use for this.

#You can reverse a string by doing the following.

string = "Hello world!"
print(string[::-1])
# This will result in "!dlrow olleH"

# Letters in a string can be changed to upper or lower case using the following.

string = "Hello world!"
print(string.upper())
print(string.lower())
# Note the brackets used to call the function.

# A string can be used to give boolean output.

string = Hello world!
print(string.startswith("Hello"))
print(string.endswith("hello"))
print(string.endswith("sdgr")
# The top one will return True. The bottom to will return false due to case sensitivity and 
# gibberish text.

# A string can be split into more strings contained in a list. Example below breaks up "Hello"
# and "world!" and stores them separately in a list.

string = "Hello world!"
words = astring.split(" ")
print(words)
# The quoted space is what determines where the strings will be split. Individual strings could
# be retrieved from the list in normal fashion (e.g. print(words[0]) to print Hello).


# Below is some more complex code tying this all together and showing these operators used in ways
# slightly different to shown above (like their postion in a function).


s = "Strings are awesome!"
print("Length of s = %d" % len(s))
# Setting the string and printing it's length using string formatting. Length is 20.

print("The first occurrence of the letter a = %d" % s.index("a"))
# Says when the first occurance of the letter "a" is. Answer is 8

print("a occurs %d times" % s.count("a"))
# How many a's are in the string. Answer is 2.

print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
# Showing off and slicing the string into bits. (Not actually splitting)

print("String in uppercase: %s" % s.upper())
# Converting to uppercase

print("String in lowercase: %s" % s.lower())
# COnverting to lowercase

if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
# Checking how the string starts. Uses if statement so only prints if True. Note the 4 space
# indent.

if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Checking how the string ends. Again uses if statement and would not print if False. Note the
# 4 space indent.

print("Split the words of the string: %s" % s.split(" "))
# Split the string into three separate strings,
# each containing only a word

