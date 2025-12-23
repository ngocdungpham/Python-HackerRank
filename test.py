def digitize(n):
    my_list = []
    while n > 0:
        temp = n%10
        print(temp)
        my_list.append(temp)
        n = n// 10
    return my_list
print(digitize(12345))