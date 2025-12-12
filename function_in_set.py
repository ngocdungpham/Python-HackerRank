def my_function(my_set, m):
    for i in range(m):
        command = input().split()
        if command[0] == "remove":
            my_set.remove(int(command[1]))
        elif command[0] == "discard":
            my_set.discard(int(command[1]))
        elif command[0] == "pop":
            my_set.pop()
        # print(command, my_set)

if __name__ == "__main__":
    n = int(input())
    my_set = set(map(int, input().split())) 
    m = int(input())
    my_function(my_set, m)
    sum = 0
    for i in my_set:
        sum += i
    print(sum)