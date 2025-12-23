"""
Docstring for IOstream_csv
1. use csv reader
2. use DictReader
3. use csv writer
4. Use DictWriter
"""
# import csv

# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, city in reader:
#         students.append({"name": name, "city": city})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} lives in {student["city"]}")


# import csv

# students = []
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} lives in {student["home"]}")


# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students.csv", "a", newline='', encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])  # Tự động thêm newline

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})  # Tự động thêm newline
    