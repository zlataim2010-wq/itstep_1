#dz3_1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof-woof")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow")

# Example usage
dog = Dog("Oreo", 3)
cat = Cat("Mia", 2)

dog.speak()
cat.speak()

#dz3_2
class Device:
    def turn_on(self):
        print("Device is turned on")

    def turn_off(self):
        print("Device is turned off")

class Phone(Device):
    def make_call(self):
        print("Phone is making a call")

class Laptop(Device):
    def open_program(self):
        print("Laptop is opening a program")

phone = Phone()
laptop = Laptop()

phone.turn_on()
phone.make_call()
phone.turn_off()

laptop.turn_on()
laptop.open_program()
laptop.turn_off()

