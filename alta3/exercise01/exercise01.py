#!/usr/bin/env python3
import time
wordbank= ["four", "spaces"]
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]
num= int(input("Pick a student's number between 0 and 17.\n>"))
time.sleep(3)
print("The student associated with that number is " + tlgstudents[num] + "!")
time.sleep(3)
print("Fun fact about this guy: " + tlgstudents[num] + " always uses four spaces to indent.")


