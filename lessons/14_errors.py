"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

#given function
def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

try:
    # Example usage:
    divide_numbers(10, 0)
# except TypeError:
#     print("error you can not add a int and str")
# except ValueError:
#     print("error invaild argument")
#check is its a zero division error
except ZeroDivisionError:
    print("you can't divide by zero")

#check if error type found
except:
    print("error something else when wrong")
#check if there no error
else:
    print("Not thing is wrong")
#declare try done running
finally:
    print("Done example 1")




"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()

try:
    # Example usage:
    read_file("nonexistent.txt")
# except SyntaxError:
#     print("There is a syntax error")

#check for IO error
except IOError:
    print("IO error: function received incorrect input")

#check if error type found
except:
    print("error something else when wrong")
#check if there no error
else:
    print("Not thing is wrong")
#declare try done running
finally:
    print("Done example 2")

"""
Example 3: List Items
"""

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

try:
    # Example usage:
    my_list = [1, 2, 3]
    get_item(my_list, 5)
#check for look up error
except LookupError:
    print("look up error: 5 can't be found in list")

#check if error type found
except:
    print("error something else when wrong")
#check if there no error
else:
    print("Not thing is wrong")
#declare try done running
finally:
    print("Done example 3")

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

try:
    # Example usage:
    my_dict = {"a": 1, "b": 2}
    get_value(my_dict, "c")
#check for key errors
except KeyError:
    print("key error: key c not found")

#check if error type found
except:
    print("error something else when wrong")
#check if there no error
else:
    print("Not thing is wrong")
#declare try done running
finally:
    print("Done example 3")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")

try:
    # Example usage:
    process_file("example.txt")
#check if error type found
except:
    print("error something when wrong")
#check if there no error
else:
    print("Not thing is wrong")
#declare try done running
finally:
    print("Done example 3")