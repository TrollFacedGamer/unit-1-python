"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

#create list
my_list = ["cat", "dog", "parrot", "fish"]
#print list
print(my_list)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
#create new list
color_list = ["blue", "yellow", "red"]
#add green to the end of the list
color_list.append("green")
#print updated list
print(color_list)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

#create new list
fruits = ["banana", "apple", "orange", "grape"]
#remove grape from list
fruits.remove("grape")
#print updated list
print(fruits)


"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

#create new list
numbers = ["one", "two", "three"]
#replace index 1
numbers[1] = "second"
#print updated list
print(numbers)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#first append
numbers.append("fourth")
#second append
numbers.append("five")
#print updated list
print(numbers)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

#delete index 4
del numbers[4]
#print updated list
print(numbers)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

#create new variable
my_numbers = numbers[0:2]
#print new variable
print(my_numbers)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

#extend my_number with color_list
my_numbers = my_numbers + color_list
#print updated list
print(my_numbers)