#!/usr/bin/python3

print("What you gotta say? :")
x = input("")
print("I got that! Anything else? :")
while True:
    y = input("")
    if y != "STOP":
        print("I got that! Anything else? :")
    else:
        break