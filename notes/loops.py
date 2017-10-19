# There are two types of loops. "for" and "while".
# For loops iterate over a given sequence.

primes = [2, 3, 5, 7]
for prime in primes:
	print(prime)
# This will print each number successively. The name that follows "for" seems to become a variable
# that inherits data from which part of the loop it's on. (When it on the second part of the table
# it takes the second value which is 3 in this case).


# For loops can iterate over a sequence of numbers using the "range" function. range is zero based
# so range(5) would be 0,1,2,3,4

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2): # The 2 at the end instructs skipping like with string operators
    print(x)

# While loops will repeat as long as a certain boolean condition is met.

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# "break is used to exit a loop (for or while) and continue is used to skip the current block and
# return to the for or while statement.

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0: # Checking for remainders after division by two. Even numbers will divide
        continue   # and will therefore have a modulo (%) of zero.
    print(x)


# else can be used in loops. break will skip the else part of the loop. It will run if
# there is a continue statement. Acts like a final instruction once a for or while loop naturally
# runs it course

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("loop broken with break and not failed")



# Excercise. Loop through and print out all even numbers from the numbers list in the same order
# they are received. Don't print any numbers that come after 237 in the sequence.



numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]

# Solution
for number in numbers: # "number" could be substituted for just about anything. "x" worked
    if number == 237:
        break	       # Don't forget to colons, they allow for the code to roll onto the next
                       # logic
    if number % 2 == 1:
        continue

    print(number)
