if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # 3713081631934410656
    t = tuple(integer_list)
    print(hash(t))
    