#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")

## Notice how the next line has changed 
## Here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
exit_q = input("Want to exit the program? y/n?")
if exit_q.lower() == "y":
    print("Goodbye.")
if exit_q.lower() == "n":
    print("I don't care. I'm leaving anyways. Goodbye.")
