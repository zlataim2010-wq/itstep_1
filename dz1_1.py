#dz1
name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")

print(f"Привіт {name}, тобі {age}!")

#dz2
age = int(input("Введіть ваш вік: "))

if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

#dz3
import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Спробуй вгадати!")

while attempts > 0:
    guess = int(input("Введи число: "))

    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")

    attempts -= 1
    print("Залишилось спроб: ", attempts)

if attempts == 0:
    print(f"Спроби закінчились. Я загадав число {secret_number}.")
