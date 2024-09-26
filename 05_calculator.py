#say welcome
print("Welcome to the Calculatinator-inator 9000!")

#ask for input
input_1 = input("Enter the first number:")
input_2 = input("Enter the second number:")

#check if input is purely numbers
if input_1.isnumeric() and input_2.isnumeric():
    #if so continue

    #convert inputs to int
    number_1 = int(input_1)
    number_2 = int(input_2)

    #list out operations
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponential")
    print("7. Remainder")

    #ask for operation
    input_operation = input("Enter choice:")

    #check if input is valid
    if input_operation.isnumeric() and int(input_operation) <= 7:
        #if so continue

        #convert inputted operation into number
        selected_operation = int(input_operation)

        #match num with operation
        if selected_operation == 1:
            #Addition
            result = number_1+ number_2
            print("Result:{}".format(result))
        elif selected_operation == 2:
            #Subtraction
            result = number_1 - number_2
            print("Result:{}".format(result))
        elif selected_operation == 3:
            #Multiplication
            result = number_1 * number_2
            print("Result:{}".format(result))
        elif selected_operation == 4:
            #Division

            #check if num_2 is =0
            if number_2 == 0:
                print("you can't divide by zero")
            else:
                #continue if not
                result = number_1 / number_2
                print("Result:{}".format(result))
        elif selected_operation == 5:
            #Floor Division
            result = number_1 // number_2
            print("Result:{}".format(result))
        elif selected_operation == 6:
            #Exponential
            result = number_1 ** number_2
            print("Result:{}".format(result))
        elif selected_operation == 7:
            #Remainder
            
            #check if num_2 is =0
            if number_2 == 0:
                print("you can't divide by zero")
            else:
                #continue if not
                result = number_1 % number_2
                print("Result:{}".format(result))
    else:
        #print error report if not
        print("you can't input a letter or a unsupported operation")

else:
    #print error report if not
    print("you inputted a letter instead of a number")