"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

#float variable
float_variable = 1.0
#convert x to int
integer_variable = int(float_variable)
#print
print(float_variable)
print(integer_variable)


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
#input > float
num = float(input("pick_a_number"))

#if-elif-else statements
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
#input > int
a = int(input("pick_a_integer"))
#input > float
b = float(input("pick_a_float"))

#math addtion
add = a + b
#math subtraction
sub = a - b
#math multiplication
mult = a * b
#math division
div = a / b

#print
print(add)
print(sub)
print(mult)
print(div)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

#dictionary
dictionary = {
    "apple" : 12,
    "orange" : 10,
    "grape" : 20,
    "lemon" : 5
}
#print
print(dictionary["apple"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

#string
my_string = "0 1 2 9 3 2"
#converting my_string to list to tuple
my_list = my_string.split(" ")
my_tuple = tuple(my_list)
#print
print(my_string)
print(my_tuple)