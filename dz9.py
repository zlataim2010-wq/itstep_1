import sqlite3

db = sqlite3.connect("AnimalKingdom.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Animals (ID INTEGER PRIMARY KEY, Name TEXT, Type TEXT)")

cursor.execute("INSERT INTO Animals (Name, Type) VALUES ('Лев', 'Ссавець')")
cursor.execute("INSERT INTO Animals (Name, Type) VALUES ('Крокодил', 'Плазун')")
cursor.execute("INSERT INTO Animals (Name, Type) VALUES ('Орел', 'Птах')")
cursor.execute("INSERT INTO Animals (Name, Type) VALUES ('Морська черепаха', 'Плазун')")
cursor.execute("INSERT INTO Animals (Name, Type) VALUES ('Мавпа', 'Ссавець')")

db.commit()

cursor.execute("UPDATE Animals SET Name='Сокіл' WHERE Name='Орел'")
db.commit()

print("Ссавці:")
for row in cursor.execute("SELECT * FROM Animals WHERE Type='Ссавець'"):
    print(row)

print("\nУсі звірі:")
for row in cursor.execute("SELECT * FROM Animals"):
    print(row)

db.close()