"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

#ask user for a string
given_string = input("give_a_string")
#repeat for each character in a string
for x in given_string:
    #print each charater
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

#create list of numbers
given_list = [0, 1, 2, 3, 4]
#create variable to store the result
result = 0
#
for x in given_list:
    result += x
#print the result
print(result)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

#create a variable that sores a sentence
sentence = "Hello nice to meet you"
#turn the sentence into a list
split_sentence = sentence.split(" ")
#iterate for each string in list
for x in split_sentence:
    #print the lenght of string
    print(len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

#create a dictionary with 4 keywords and values
four_value_dictionary = {
    "wang":"benny",
    "appleseed": "johnny",
    "yang": "ling",
    "lin": "andy"
}

#iterate each keyword and value set
for x in four_value_dictionary:
    #print the keyword of the iterated set
    print(x)

#I notice that the output of my code is just the key words of the dictionary. 
#This did not meet my expection as i was expecting the keywords and the values to be printed at the sametime.