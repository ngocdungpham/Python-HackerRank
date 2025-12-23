# with open("Students.csv", "r", encoding="utf-8") as file:
#     for line in file:
#         name, city = line.strip().split(",")
#         print(f"{name} live in {city}")
        
students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)

for student in students:
    print(f"{student['name']} live in {student['city']}")

# for student_ in sorted(students, key=lambda x: x, reverse=False):
#     print(f"{student[0]} live in {student[1]}")