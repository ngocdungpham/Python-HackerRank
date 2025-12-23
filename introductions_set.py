def average(array):
    my_set = []
    for i in array:
        if i not in my_set:
            my_set.append(i)
    sum = 0
    for i in my_set:
        sum += i
    return sum/len(my_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)