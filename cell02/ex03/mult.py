#!/usr/bin/python3

x = int(input("plese enter first number :"))
y = int(input("plese enter second number :"))
result = x * y
print(result)
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is both positive and negative")