#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") #This line prompts the user for input

# a provided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk) #intended under if
else: #if data is not provided
    print("You did not provide an input, idiot. How about you get smart and try again.")

