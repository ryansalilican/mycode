#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n************Details of Interface - ', i , ' ************')
    print(netiface.ifaddresses(i))

