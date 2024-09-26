'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
#integer
integer = 19
#check if even and >10
even_greater = integer % 2 == 0 and integer > 10
#print
print(even_greater)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
#variable person's age
person_age = 18
#variable if person is student
is_student = False
#check if <18 or student?
if person_age < 18 or is_student:
    #print $10 if conditions are true
    print("Price_is_$10")
else:
    #print $20 if conditions are false
    print("Price_is_$20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
#ask for a fruit name
fruit = input("name_a_fruit")
#list of fruits
fruits = ["apple", "orange", "coconut", "banana", "grape"]
#check if given is in list
if fruit in fruits:
    #print when coditions are true
    print("Yes, that fruit is in the list.")
else:
    #print when coditions are false
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

#ask year, convert to integer
year = int(input("what_year_is_it?"))
#check if year is divisible by four
if year % 4 == 0:
    #print leap year if true
    print("it_is_a_leap_year.")
else:
    #print century year if false
    print("it_is_a_century_year.")

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

#ask for weight, convet to int
weight = int(input("what_is_the_weight_of_shipped_object in Kg?"))
#ask for destination zone
destination_zone = input("what_is_the_destination_zone?")
#print error if weight is <0
if weight < 0:
    print("error")
#print weight time 5 dollars
elif destination_zone == "A":
    print("$" + str(weight * 5))
#print weight time 7 dollars
elif destination_zone == "B":
    print("$" + str(weight * 7))

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

#ask for side lenghts
side_lenghts = input("give the lenght of a triangle's sides").split(" ")
#check if shape have 3 sides
if len(side_lenghts) == 3:
    if side_lenghts.count(side_lenghts[0]) == 3 or side_lenghts.count(side_lenghts[1]) == 3 or side_lenghts.count(side_lenghts[2]) == 3:
        print("this is a equilateral triangle")
    elif side_lenghts.count(side_lenghts[0]) == 2 or side_lenghts.count(side_lenghts[1]) == 2 or side_lenghts.count(side_lenghts[2]) == 2:
        print("this is a isosceles triangle")
    elif side_lenghts.count(side_lenghts[0]) == 1 or side_lenghts.count(side_lenghts[1]) == 1 or side_lenghts.count(side_lenghts[2]) == 1:
        print("this is a scalene triangle")
else:
    print("this is not a triangle")