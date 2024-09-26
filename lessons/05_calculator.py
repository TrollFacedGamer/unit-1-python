print("Welcome to the Calculatinator-inator 9000!")

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

selected_operation = int(input("Enter choice:"))

if selected_operation == 1:
    result = number_1+ number_2
elif selected_operation == 2:
    result = number_1 - number_2
elif selected_operation == 3:
    result = number_1 * number_2
elif selected_operation == 4:
    result = number_1 / number_2
elif selected_operation == 5:
    result = number_1 // number_2
elif selected_operation == 6:
    result = number_1 ** number_2
elif selected_operation == 7:
    result = number_1 % number_2

print("Result:{}".format(result))
    