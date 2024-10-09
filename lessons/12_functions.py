"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#define function with hello parameter
def hello_name(name):
    
    #print Hello with variable name
    print(f"Hello, {name}")

#ask user for name
hello_name(input("What is you name?"))

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#import sqrt function
from math import sqrt

#define function with num argument
def square(num):

    #return sqrt of num
    return(sqrt(num))

#ask user for integer
square(int(input("Give a integer.")))


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

#define function with number argument
def even_odd(number):

    #return if num has remainder with 2
    return(number % 2 == 0)

#ask user for number
even_odd(int(input("Give a number.")))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

#define function with lenght&width argument
def area_of_rectangle(lenght, width):
    
    #return product of arugments
    return(int(lenght) * int(width))

#ask user for lenght and width
area_of_rectangle(input("Give lenght"),input("Give width."))

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

#define function with celsius argument
def celsius_to_fehrenheit(celsius):
    
    #return the product of equation
    return((int(celsius) * (9/5)) + 32)

#ask user for celsius
celsius_to_fehrenheit(input("Give a celsius"))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

#define function with list_of_num arugment
def mean(list_of_num):
    #define counter
    average = 0
    #add up all the numbers
    for x in list_of_num:
        average += int(x)
    
    #return total / lenght of list
    return(average / len(list_of_num))

#call function with list
mean([5, 10, 15, 20, 25])


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

#define function with 3 arguments
def total_calculator(price, quantity, discount):
    
    #check if there's a discount
    if discount == 0:
        #return the base price
        return("Total: $" + str(price * quantity))
    else:
        #return discount and discounted price
        return("Total: $" + str(price * quantity) + ", " + "Discount:" + discount + ", " + "Discounted Total: $" + str(price * quantity * discount))

#call function with 3 inputs
total_calculator(12, 2, 0.5)
