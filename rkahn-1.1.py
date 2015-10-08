#!/usr/bin/env python

lower = 0
upper = 100

print "*Number Guessor*"
print "Think of a number between " + str(lower) + " and " + str(upper) + ", and I will try to guess it."

while True:
    
    # ask whether it is the midpoint of remaining available numbers
    midpoint = ((upper - lower) / 2) + lower
    data_input = raw_input("is it " + str(midpoint) + " (yes/no/quit)?   ")
    
    # if yes, announce victory
    if data_input == "yes":
        print "Awesome! I win!"
        break
    
    # if no, ask if higher or lower, and adjust remaining available numbers, reloop
    elif data_input == "no":
        highlow_input = raw_input("Is it higher or lower than " + str(midpoint) + "?  ")
        if highlow_input == "higher":
            lower = midpoint + 1
        elif highlow_input == "lower":
            upper = midpoint - 1
        else:
            print highlow_input + "was not one of the options."
            continue
    
    # if quit, end
    elif data_input == "quit":
        break
    
    # if user types something else, inform them and reloop
    else:
        print data_input + " was not one of the options."
        continue
