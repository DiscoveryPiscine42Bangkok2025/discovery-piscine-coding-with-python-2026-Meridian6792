#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in array if x > 5]
new_array = list(set(new_array))  
print("Original array:", array)
print("New array:", new_array)
