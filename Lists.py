if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command = input().split()
        # print(command)
        if command[0] == "print":
            print(list)
        elif command[0] == "insert" and len(command) == 3:
            list.insert(int(command[1]), int(command[2]))
            # print(len(list))
        elif command[0] == "append" and len(command) == 2:
            list.append(int(command[1]))
        elif command[0] == "remove" and len(command) == 2:
            list.remove(int(command[1]))
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "pop":
            if list:
                list.pop()
            else:
                print("Error: Cannot pop from an empty list.")
        elif command[0] == "reverse":
            list.reverse()
        # print(list)
