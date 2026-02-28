import random

class Student:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.knowledge = 0
        self.motivation = 100

    def study(self):
        print("Студент навчається в ITStep...")
        self.knowledge += random.randint(5, 15)
        self.energy -= random.randint(10, 20)
        self.motivation -= random.randint(5, 10)

    def rest(self):
        print("Студент відпочиває...")
        self.energy += random.randint(10, 20)
        self.motivation += random.randint(5, 10)

    def code(self):
        print("Студент пише код...")
        self.knowledge += random.randint(10, 20)
        self.energy -= random.randint(15, 25)

    def show_status(self):
        print("\n--- СТАТУС ---")
        print(f"Ім'я: {self.name}")
        print(f"Енергія: {self.energy}")
        print(f"Знання: {self.knowledge}")
        print(f"Мотивація: {self.motivation}")
        print("--------------\n")

    def is_alive(self):
        return self.energy > 0 and self.motivation > 0


name = input("Введіть ім'я студента: ")
student = Student(name)

print(f"\nЛаскаво просимо до ITStep, {name}!\n")

while student.is_alive():
    student.show_status()
    print("Оберіть дію:")
    print("1 - Навчатися")
    print("2 - Відпочити")
    print("3 - Писати код")
    print("4 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        student.study()
    elif choice == "2":
        student.rest()
    elif choice == "3":
        student.code()
    elif choice == "4":
        break
    else:
        print("помилка")

if student.energy <= 0:
    print("Студент перевтомився!!")
elif student.motivation <= 0:
    print("Студент втратив мотивацію...")
else:
    print("До зустрічі в ITStep!")