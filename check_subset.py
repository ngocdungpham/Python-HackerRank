def check_subset(my_set_A, my_set_B):
    my_set_ans = my_set_A.intersection(my_set_B)
    return True if len(my_set_A) == len(my_set_ans) else False

if __name__ == "__main__":
    n = int(input())
    while n > 0:
        len_1 = int(input())
        my_set_1 = set(map(int, input().split()))
        len_2 = int(input())
        my_set_2 = set(map(int, input().split()))
        if check_subset(my_set_1, my_set_2):
            print("True")
        else:
            print("False")
        n -= 1