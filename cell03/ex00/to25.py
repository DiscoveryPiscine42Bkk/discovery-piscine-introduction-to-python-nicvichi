#!/usr/bin/python3

number = int(input("enter a number less than 25:"))
if number < 25:
    for x in range(number,26):
        print("Inside the loop,my viriable is",x)
else:
    print("Error")