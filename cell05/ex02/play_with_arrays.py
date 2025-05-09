#!/usr/bin/python3

array1 = -42
array2 = -28
array3 = -14
array4 = 0
array5 = 14
array6 = 28
array7 = 42
Original_array = [-42,-28,-14,0,14,28,42];
New_array = [];
print(Original_array)
for x in range(len(Original_array)):
    if Original_array[x] > 5:
        New_array.append(Original_array[x] + 2)
print(New_array)