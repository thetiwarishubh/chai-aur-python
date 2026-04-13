# Encapsulation (Data ko protect karna)

class Bank :
    def __init__(self):

        self.__balance = 0 # Private 

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    

sbi_bank = Bank()
sbi_bank.deposit(10000)
print(sbi_bank.get_balance())


# 2. Inheritance (Code reuse 💀)
class Animal :
    def speak(self):
        print("Animal speaks")


class Dog(Animal) :
    def bark(self) :
        print("Dog Barks")


german_shepherd = Dog()
german_shepherd.speak()
german_shepherd.bark()

# 🎭 3. Polymorphism (Same kaam, different behavior)

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()