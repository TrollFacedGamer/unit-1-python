"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

#import the datetime function
from datetime import datetime
#put current datetime in variable
curret_date_and_time = datetime.now()
#print variable
print(curret_date_and_time)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#import the date function
from datetime import date
#put current date in variable
curret_date = datetime.now()
#format
US_standard = curret_date.strftime("%m/%d/%Y")
#print variable
print(US_standard)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

#create date strings
string_1 = "01/18/2021"
string_2 = "02/9/2021"
#convert strings to date
date_1 = datetime.strptime(string_1, "%m/%d/%Y")
date_2 = datetime.strptime(string_2, "%m/%d/%Y")
#find differnce
differnce = date_2 - date_1
#print diffrence
print(differnce)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#ask for birthday
ask = input("what is your birthday?")
#convert
birthday = datetime.strptime(ask, "%m/%d/%Y")
#find today
today = datetime.now()
#find diffrence
age_in_days = today - birthday
#print difference
print(age_in_days)