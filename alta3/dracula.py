#!/usr/bin/env python3
import os
import shutil

with open("dracula.txt", "r") as book:
    count = 0
    for line in book:
        if "vampire" in line.lower():
            print(line)

