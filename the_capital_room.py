# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
def count_frequency_manual(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for key, value in freq.items():
        if value == 1:
            return key
if __name__ == "__main__":
    n = int(input())
    my_list = list(input().split())
    data = [1, 2, 2, 3, 3, 3, 4, 1, 2]
    print(count_frequency_manual(my_list))