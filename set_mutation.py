A = int(input())
my_set = set(map(int, input().split()))
n = int(input())

while n > 0:
    command = input().split()
    my_set_2 = set(map(int, input().split()))
    # print(f"my_set_2: {my_set_2}")
    if int(command[1]) != len(my_set_2):
        print("Thieu phan tu") 
        continue
    if command[0] == "intersection_update":
        my_set.intersection_update(my_set_2)
    elif command[0] == "update":
        my_set.update(my_set_2)
    elif command[0] == "difference_update":
        my_set.difference_update(my_set_2)
    elif command[0] == "symmetric_difference_update":
        my_set.symmetric_difference_update(my_set_2)
    # print(my_set)
    n -= 1
print(sum(my_set))