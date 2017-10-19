# Math operators can be used with numbers

number = 1 + 2 *3 / 4.0
print(number)
# Note that integers and floating numbers can be mixed

#Another operation is modulo. This one is weird and returns the remainder after division

remainder = 11 % 3
print(remainder)
# 3 goes into 11 three times (9) with a remainder of 2

# Two multiplication symbols makes power.

squared = 2 ** 2
cubed = 2 ** 3
print(squared, cubed)

# Operators can be used with strings.

helloben = "hello" + " " + "Ben"
print(helloben)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# And lists.

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [ 2, 4, 6, 8]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1 ,2, 3] * 3)
