#one
# temperature = 75

# if temperature > 80:
#     print("It's hot")
# elif temperature > 50:
#     print("It's temperate")
# elif temperature < 0:
#     print("It's cold")

#two
# text = "Hello, world, my name is"
# count = 0

# for char in text:
#     if char == " ":
#        count += 1

# print(count)

#three
# print("give me a number")
# n = int(input())

# for num in range(1, n):
#     if num % 2 == 0:
#         print(num, "is even.")
#     else:
#         print(num, "is odd.")

#four
# num = int(input("Enter an integer: "))

# if num < -1:
#   print("No negative numbers.")
# else:
#   result = 1
#   for i in range(1, num + 1):
#     result *= i   

#   print("Factorial of " + str(num) + " is " + str(result))

#five
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
    else:
        print("Incorrect password")

    if attempts >= 3:
        print("Too many attempts")
        break