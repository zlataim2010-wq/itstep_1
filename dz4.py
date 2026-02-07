class Car:
    def __init__(self, model):
        self.model = model

    def show_info(self):
        print("Car model:", self.model)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def drive(self):
        print(self.name, "is driving a", self.car.model)


# Example simulation
car = Car("Toyota")
driver = Driver("John", car)

car.show_info()
driver.drive()