"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#define function with hello parameter
def hello_name(name):
    '''takes a parameter
        Print sentence.
    '''

    #print Hello with variable name
    print(f"Hello, {name}")

#ask user for name
hello_name(input("What is you name?"))
print(hello_name.__doc__)

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#import sqrt function
from math import sqrt

#define function with num argument
def square(num):
    '''takes a parameter(number)
        Return a sqrt.
    '''

    #return sqrt of num
    return(sqrt(num))

#ask user for integer
print(square(9))
print(square.__doc__)


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

#define function with number argument
def even_odd(number):
    '''take a parameter(number)
        Determine if even
        Return True/False.
    '''

    #return if num has remainder with 2
    return(number % 2 == 0)

#ask user for number
even_odd(int(input("Give a number.")))
print(even_odd.__doc__)


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

#define function with lenght&width argument
def area_of_rectangle(lenght, width):
    '''takes 2 parameters(lenght & width)
        Return area.
    '''
    
    #return product of arugments
    return(int(lenght) * int(width))

#ask user for lenght and width
print(area_of_rectangle(5,5))
print(area_of_rectangle.__doc__)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

#define function with celsius argument
def celsius_to_fehrenheit(celsius):
    '''takes a parameter(celsius)
        Return fehrenheit.
    '''
    
    #return the product of equation
    return((int(celsius) * (9/5)) + 32)

#ask user for celsius
print(celsius_to_fehrenheit(32))
print(area_of_rectangle.__doc__)

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

#define function with list_of_num arugment
def mean(list_of_num):
    '''take a parameters(list of numbers)
        Return mean
    '''

    #define counter
    average = 0
    #add up all the numbers
    for x in list_of_num:
        average += int(x)
    
    #return total / lenght of list
    return(average / len(list_of_num))

#call function with list
print(mean([5, 10, 15, 20, 25]))
print(mean.__doc__)


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

#define function with 3 arguments
def total_calculator(price, quantity, discount):
    '''take parameters(price, quantity, discount)
        Determine if discount = 0
        Return price or price, discount, discounted price
    '''
    
    #check if there's a discount
    if discount == 0:
        #return the base price
        return("Total: $" + str(price * quantity))
    else:
        #return discount and discounted price
        return("Total: $" + str(price * quantity) + ", " + "Discount:" + discount + ", " + "Discounted Total: $" + str(price * quantity * discount))

#call function with 3 inputs
total_calculator(12, 2, 0.5)
print(total_calculator.__doc__)
