names = []
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names, key=lambda x : (len(x), x), reverse=True):
    print(name)