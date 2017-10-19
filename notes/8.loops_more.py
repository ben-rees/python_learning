# Quick addition to the lsits stuff. There's a min/max command
# Seems useful for conditional stuff

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
# A list...or Array apparently

for element in a:
    if element == max(a): # Checks for highest value in specified list
        print(element*"=") # Prints = the same number of times as the value
                           # of element
        print("Largest number reached")
    print(element*"=")
