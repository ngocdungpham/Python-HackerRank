m = int(input())
a = set()
for i in range(m):
    x = int(input())
    a.add(x)

n = int(input())
b = set()
for i in range(n):
    x = int(input())
    b.add(x)

symmetric_difference = a.symmetric_difference(b)
for item in sorted(symmetric_difference):
    print(item)
