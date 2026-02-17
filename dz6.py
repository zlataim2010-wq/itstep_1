try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    y = "5" + 5
except TypeError as e:
    print("TypeError:", e)

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError:", e)

try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print("KeyError:", e)

try:
    number = int("hello")
except ValueError as e:
    print("ValueError:", e)

try:
    file = open("nofile.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)