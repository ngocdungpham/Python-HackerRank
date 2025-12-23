def check_strict_superset(my_set_1, my_set_2):
    my_set_ans = my_set_2.intersection(my_set_1)
    return True if len(my_set_ans) == len(my_set_2) else False

if __name__ == "__main__":
    my_set = set(map(int, input().split()))
    n = int(input())
    ans = True
    while n > 0:
        my_set_check = set(map(int, input().split()))
        if check_strict_superset(my_set, my_set_check) == False:
            ans = False
            break
        n -= 1
    print(ans)
