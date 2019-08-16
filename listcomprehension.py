import os
#! /usr/bin/python3

list_num = [2.2, 1.3, 8.8, 5.5, 3.4, 12.5, 9.9, 2.7, 7.1, 1.1]
# SYNTAX
# list_name = [{operation} {for loop} {condition (if needed)}] # curly brackets are not used

# use list comprehension to do the following:
#  1) create list of the squares of all the numbers
squares_list = [n**2 for n in list_num]
print(squares_list)

#  2) create a list of lists of the squares and cubes of all the numbers
squares_cubes_list = [[n**2, n**3] for n in list_num]
print(squares_cubes_list)

#  3) create a list of the output of this operation on each number:
#     ((n + 3,299) / n)**3
operation_list = [((n + 3299) / n)**3 for n in list_num]
print(operation_list)

#String Manipulation

string = "Aaron, Iddy, John, Rachel, Stephen, Ibrahim, Titus, Zephrin, Makuru, Christina"

# convert this string into a list, then use list comprehension
# to do the following:
string_list = string.split(", ")
print(string_list)

# 1) make a list of all the names lowercase
lower = [str.lower() for str in string_list]
print(lower)
