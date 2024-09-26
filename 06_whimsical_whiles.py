"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

#create counter
i = 1
#repeat till i is not <= 10
while i <= 10:
    #print i first to inculde 1
    print(i)
    #add 1 to i each iteration
    i += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#create variable as counter
x = 10
#repeat till x not >= 1
while x >= 1:
    #print x first, inculde 10
    print(x)
    #subtract 1 to i each iteration
    x -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

#create counter
y = 10
#repeat till variable not >0
while y > 0:
    #print first to inculde 10*10
    print(10 * y)
    ##subtract 1 to i each iteration                                                                                    
    y -= 1

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#create password storage variable
password = "123apple"
#create user input vaiable
password_input = 0
#repeat till input is == password
while password_input != password:
    #ask user for input password
    password_input = input("what_is_the_password?")
    #say it is incorrect 
    if password_input != password:
        print("incorrect")
    #say it is correct
    elif password_input == password:
        print("correct")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

#repeat counter
repeat = 0
#to store sum
result = 0
#ask for number
given_number = input("give a number")
#repeat till repeat is 1 less
while repeat < len(given_number):
    #add digits to result
    result += int(given_number[repeat])
    #add counter
    repeat += 1
#print sum
print(result)

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

#ask for how many
n = int(input("how_many_numbers_do_you_want?"))
#list to store the sequence
fibonacci_sequence = [0, 1]
#repeat counter
repeat_1 = 0
#lenghten the fibonacci_sequence as need
while len(fibonacci_sequence) < n:
    fibonacci_sequence.append(fibonacci_sequence[len(fibonacci_sequence) - 2] + fibonacci_sequence[len(fibonacci_sequence) - 1])
#print each value in list
while repeat_1 < n:
    print(fibonacci_sequence[repeat_1])
    repeat_1 += 1

