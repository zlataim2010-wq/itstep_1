class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 5

    def eat(self):
        self.energy += 1
        print(self.name, "поїв")

    def play(self):
        self.energy -= 1
        print(self.name, "погрався")

    def status(self):
        print("Енергія:", self.energy)
dog = Dog("Громіт")

dog.status()
dog.play()
dog.eat()
dog.status()