#!/usr/bin/env python3

import random
num= random.randint(1,100)

while True:
    guess= int(input("Provide your number guess from 1-100: \n>"))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct! Great job!")
        break

