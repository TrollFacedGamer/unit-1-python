"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

#interate from 1 though 10
for x in range(1, 11):
    #print the value of x
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

#interate from 900-1000 by 10
for x in range(900, 1001, 10):
    #print x seconds
    print(str(x) + "s")

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

#interate from 1-100 by 9
for x in range(1, 101, 9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#variable to store calculated sum
sum = 0
#interate from 1 to 10
for x in range(1, 11):
    #add interation to sum
    sum += x

print(sum)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
  the out put of the code is a right triangle made of *s with a decending slope and a vertical and horizontal line.
- Explain the iterative process that this code executes to get that output
  the code repeat for 0 to 4 and for each number between 0 and 4 lay down a equivalent number of *(s) and spaces, before doing a equivalent of return with a blank print.
"""
#the variable set the number of times the code is iterated which 5 times.
rows = 5
#i is interated as numbers 0-4 due to how range starts with 0 unless commanded otherwise.
for i in range(rows):
    #interate for the value of i + 1
    for j in range(i + 1):
        #print * with a space each interation
        print('*', end=' ')
    #print nothing to do the equivalent of return
    print()