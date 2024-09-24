"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

#create a variable as a counter
i = 1
#repeat till i is no longer <= 10 to inculde and end at10
while i <= 10:
    #print i first to inculde 1
    print(i)
    #add 1 to i in each iteration
    i += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#create variable as counter
x = 10
#repeat till x is no longer >= 1 to inculde and end at 1
while x >= 1:
    #print x first to inculde 10
    print(x)
    #subtract 1 to i in each iteration to create decending order
    x -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

#create variable as counter
y = 10
#repeat till variable is no longer greter then 0
while y > 0:
    #print first to inculde 10*10
    print(10 * y)
    ##subtract 1 to i in each iteration to create decending order to muitply with                                                                                           
    y -= 1

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#create password storage variable
password = "123apple"
#create user input vaiable
password_input = 0
#repeat till user input is = to password
while password_input != password:
    #ask user for input password
    password_input = input("what_is_the_password?")
    #if password is incorrect say it is incorrect 
    if password_input != password:
        print("incorrect")
    #if password is correct say it is correct
    elif password_input == password:
        print("correct")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

n = int(input("how_many_numbers_do_you_want?"))
number1 = 0
number2 = 1
repeats = 0
while repeats < n:
    print(number1)
    print(number2)
    number2 = number1 + number2
    number1 = number2 - number1
    repeats += 1
