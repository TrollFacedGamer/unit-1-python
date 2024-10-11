class Character:
    health = 20

    #functions in class is called method, only needed if you want to change variable unpon object creation
    def __init__(self, name):
        self.name = name
        
    def damage(self, dmg):
        self.health = self.health - dmg

class Player(Character):
    health = 50

    def heal(self):
        if self.health < 50:
            self.health = self.health + 1

enemy = Character("Balthazar")
enemy.damage(12)
print(enemy.health)

player1 = Player("Forlenza")
player1.damage(12)
player1.heal()
print(player1.health)

"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age
    def introduce(self):
        print(f"Hello I am {self.name} and I am {self.age} year old")

benny = Person("Benny", 16)
benny.introduce()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal:
    voice = ""
    def speak(self):
        print(self.voice)

class Dog(Animal):
    voice = "Woof"

class Cat(Animal):
    voice = "meow"

dog1 = Dog()
dog1.speak()
cat1 = Cat()
cat1.speak()



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""



        