"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

#password
password = "hello123."
#ask for password and set it to all lower case
entered_password = input("what_is_the_password?").lower()
#check if given password match the stored password
if password == entered_password:
    print("correct")
else:
    print("incorrect")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

#ask for user input and strip it
user_input = input("what_would_you_like?").strip()
#use boolean to check if input is empty
not_empty = bool(user_input)
#print valid when not_empty is true and invaild when it is something else.
if not_empty == True:
    print("valid")
else:
    print("invalid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

#base sentence
sentence = "The_cat_is_angry._Cats_can_get_angry."
#decapitalize
lowercase = sentence.lower()
#change cat to dog
edited_sentence = lowercase.replace("cat", "dog")
#print base sentence
print(sentence)
#print changed sentence
print(edited_sentence)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

#ask for name
name = input("what_is_your_name?")
#ask for age
age = input ("what_is_your_age?")
#write a sentence using the inputs
name_and_age = f"{name}_is_{age}."
#print made sentence
print(name_and_age)


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

#ask for 2 different floats in str before converting to float
float1 = float(input("give_a_float."))
float2 = float(input("give another float."))
#divide the 1st float by the 2nd float
quotient = float1 / float2
#round to the nearest 1 decimal place
round_tenth = "{:.1f}".format(quotient)
#print results
print(round_tenth)
