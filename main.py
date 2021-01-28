import hello_world

import math
import random
import copy

# use import to use hello_world.py

# data types
# int, float, double, str, list, typle, dict, set, etc.
x = 10
print(x, type(x))
x = "hello"
print(x, type(x))

# operators
# / floating point div
# // int div
# ** exponentiation
# can also use math.pow() (and other functions...)
print(math.pow(2,5))

# user input
# fav_num = int(input("Enter your favorite number: "))
# print(fav_num, type(fav_num))

# conditionals
temperature = 37
if temperature > 32:
    print("It is warm outside")
else:
    print("it is cold outside")
# use elif for else if

# loops
# while and for loops
# for (int i = 0; i < 5; i++) { }
# for item in sequence:
#   body
for i in range(5): # [0, 5) incrementing by 1
    print(i, end = " ") # default end is new line
print()

# warm up task
# e.g. 2, 4, ..., 38, 40
def print_even_numbers(stop=40):
    for i in range(2, stop, 2):
        print(i, end=", ")
    print(i + 2)

# functions
# start with def
# they can accept keywaord args
# call the function
print_even_numbers(20)
print_even_numbers()

# random numbers (import random)
# seed the generator for reproducibility
random.seed(0)
die_roll = random.randint(1, 6) # [1, 6]
print(die_roll)

# decimal formatting
# 3 ways to round to 2 decimal places
print(math.pi, round(math.pi, 2))
# C style
print("%.2f" %(math.pi))
# Pythonic
print("{:.2f}".format(math.pi))

# lists
# like arrays, but can grow/shrink in size
# lists are objects, they have methods
# <object>.<method>()
# can have mixed types
fibs = [1, 1, 2, 3, 5, 8]
print(fibs)
# use loops
# [0] [1]...
for value in fibs:
    print(value)
# use len() to get hte number of items in the list
for i in range(len(fibs)): 
    print(i, ":", fibs[i])

# built in functions
print(sum(fibs))
print(max(fibs))

# list methods
fibs.append(13)
print(fibs)

# nested lists
# we will use a nested list (e.g 2D list) to store tabular data
matrix = [[0, 1, 2], [3, 4, 5]] # 2x3 table
print(matrix)

# task: define/call a pretty_print(table)
# prints the nested list in a nice grid structure
# 0 1 2
# 3 4 5
def pretty_print(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print()

pretty_print(matrix)

# ptyhon is pass by OBJECT REFERENCE
# object references are passed by value
def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

def clear_out(table):
    table = []

print("matrix before:", matrix)
add_one(matrix)
print("Matrix after:", matrix)

print("matrix before:", matrix)
clear_out(matrix)
print("Matrix after:", matrix)

# shallow vs deep copy
matrix_copy = matrix.copy() # makes a shallow copy
# shallow copy: copies the references to objects, not
# the objects themselves
matrix_deep_copy = copy.deepcopy(matrix) # deep copy
# deep copy: copies the objects themselves

print("matrix before:", matrix)
print("matrix copy before:", matrix_copy)
print("matrix deep copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix copy after:", matrix_copy)
print("matrix deep copy after:", matrix_deep_copy)

# moral of the story: you probably want a deep copy

# file IO
# we want to load the contents of a csv file into a table (e.g. nested list)
# comma separated value file

def read_table(filename):
    table = []
    # 1. opepn
    infile = open(filename, "r")
    # 2. process (read/write)
    lines = infile.readlines()
    # need to convert "numeric values" to a numeric type
    # input example: int() float()
    print(lines)
    # TODO: next class

    # 3. close

    return table

table = read_table("msrp.csv")
print(table)