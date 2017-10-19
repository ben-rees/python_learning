# Funtions are a way to divide code into blocks making it easier to work with and share.

# To begin with Python makes use of blocks

block_head:
	block_line
	block_line
# Block head would be something like if, for, while, else etc. block_lines are the code that
# follows like print() etc.

# Functions are defined by using "def" followed by the function's name as the block's name.

def my_function():
	print("Hello from my function")

#Function can also recieve arguments (variable passed from the caller to the function).

def my_function_with_args(username, greeting)
	print("Hello %s from my function! I wish you %s" %(username, greeting))

# Functions can also return a value to the caller using "return".

def sum_numbers(a, b)
	return a + b

# To call a function write the functions name followed by "()" and place any arguments inside
# the brackets.

# Defining the functions
def my_function():
    print("Hello from my function!")
def my_function_with_args(username, greeting):
    print("Hello %s from my function! I wish you %s" %(username, greeting))
def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

# prints - "Hello Ben from my function! I wish you a great year!"
my_function_with_args("Ben", "a great year!")

# after this line x will hold the value 3! The 1 & 2 are put into the function and the returned
# back to the caller below (which is 3)
x = sum_two_numbers(1,2)


# Exercise below (solved)

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    for benefit in list_benefits():
        print(build_sentence(benefit))

name_the_benefits_of_functions()
