if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = 0
    second = 0
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    print(second)