#create dictionary
dictionary = dict()

#set up a loop
while True:
    #list out choices
    print("Contact Book Menu")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. List contacts")
    print("4. Exit")
    print("")

    #ask for choice
    choice = int(input("Enter your choice: "))
    print("")

    #compare choice with if-elif chain
    #add
    if choice == 1:
        #ask for name
        name = input("Enter the name of the contact you wish to add: ")

        #ask for number
        number = input("Enter the number of the contact you wish to add: ")
        print("")

        #check if number is longer then 10
        if len(number) > 10 or number.isnumeric() == False:
            
            #repeat till requirements are met
            while len(number) > 10 or number.isnumeric() == False:
                
                #tell number requirements
                print("numbers can only be 10 numbers long and made only of numbers")
                
                #ask for number again
                number = input("Enter the number of the contact you wish to add: ")
                print("")

        #add name and num to dict
        dictionary[name] = number
    
    #delete
    elif choice == 2:

        #ask for delete key
        delete = input("Enter the name of the contact uou wish to delete: ")
        print("")

        #check if input is key
        if delete in dictionary:
            
            #delete key
            del dictionary[delete]
        else:
            #error
            print("Contact does not exist.")

    #list
    elif choice == 3:
        #print each dict separately
        for x in dictionary:
            print(str(x) + ": " + str(dictionary[x]))
        print("")

    #exit
    elif choice == 4:
        #stop loop
        break

