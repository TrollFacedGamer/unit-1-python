#create class Character
class Character:
    #create variable health
    health = 20

    '''functions in class is called method'''
    '''__init__ is only needed if you want to change variable unpon object creation'''
    
    #define name upoun object creation
    def __init__(self, name):
        self.name = name
        
    #define damage method
    def damage(self, dmg):
        #reduce health variable by dmg
        self.health = self.health - dmg

#create subclass Player
class Player(Character):
    #make new health var
    health = 50

    #create heal method
    def heal(self):
        #check if health is < 50
        if self.health < 50:
            #add to health by 1
            self.health = self.health + 1

#make object with Character
enemy = Character("Balthazar")
#use damage method
enemy.damage(12)
#check health
print(enemy.health)

#make object with subclass Player
player1 = Player("Forlenza")
#use damgage method
player1.damage(12)
#use heal method
player1.heal()
#check health
print(player1.health)

"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

#create class
class Person:
    #define attributes
    def __init__(self, name, age):
       self.name = name
       self.age = age
    #function that introduces
    def introduce(self):
        print(f"Hello I am {self.name} and I am {self.age} year old")

#create object
benny = Person("Benny", 16)
#call method
benny.introduce()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#define class Animal
class Animal:
    #create empty method speak
    def speak(self):
        pass

#define subclass Dog
class Dog(Animal):
    #give Dog unique speak method
    def speak(self):
        print("Woof")

#define subclass Cat
class Cat(Animal):
    #give Cat unique speak method
    def speak(self):
        print("meow")

#create object with Dog() subclass
dog1 = Dog()
#call speak method of object
dog1.speak()
#create object with Cat() subclass
cat1 = Cat()
#call speak method of object
cat1.speak()

'''I made this in case i did this incorrectly with the above'''
'''please ignore if the above if fine'''

#create class
class Animal_:
    #create empty variable
    voice = ""
    #create speak method with print
    def speak(self):
        print(self.voice)

#define subclass Dog
class Dog_(Animal):
    #change variable to change print
    voice = "Woof"

#define subclass Cat
class Cat_(Animal):
    #change variable to change print
    voice = "meow"


#create object with Dog() subclass
dog1 = Dog()
#call speak method of object
dog1.speak()
#create object with Cat() subclass
cat1 = Cat()
#call speak method of object
cat1.speak()

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#create class
class BankAccount:

    #create init input
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    #create method depositing
    def depositing(self, deposit_amount):
        self.balance += deposit_amount
        print(self.balance)

    #create method withdraw
    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        print(self.balance)

#create object
bank_account_1 = BankAccount(100, "Benny")

#check if object made correct
print(bank_account_1.balance)
print(bank_account_1.owner)

#check depositing method
bank_account_1.depositing(100)

#check withdraw method
bank_account_1.withdraw(50)