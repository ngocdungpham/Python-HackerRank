# def count_substring(string, sub_string):

#     count = 0
#     m = len(sub_string)
#     for i in range(len(string) - m + 1):
#         if string[i:i+m] == sub_string:
#             count += 1 
#     return count

# # def count_substring(string, sub_string):
# #     return string.count(sub_string)  # Hàm built-in, tối ưu tốt hơn

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)


def build_lps(pattern):
    """Xây dựng mảng LPS (Longest Proper Prefix which is also Suffix)"""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def count_substring(string, sub_string):
    """Đếm số lần xuất hiện của sub_string trong string sử dụng KMP - O(n + m)"""
    n = len(string)
    m = len(sub_string)
    
    if m == 0 or m > n:
        return 0
    
    lps = build_lps(sub_string)
    count = 0
    i = 0  # index cho string
    j = 0  # index cho sub_string
    
    while i < n:
        if string[i] == sub_string[j]:
            i += 1
            j += 1
        
        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and string[i] != sub_string[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)