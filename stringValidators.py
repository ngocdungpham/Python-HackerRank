if __name__ == '__main__':
    s = input()
#     if s.isalnum():
#         print("Chuoi ban vua nhap chi chua chu cai va chu so.")
#     if s.isalpha():
#         print("Chuoi ban vua nhap chi chua chu cai.")
#     if s.isdigit():
#         print("Chuoi ban vua nhap chi chua chu so.")
#     if s.islower():
#         print("Chuoi ban vua nhap chi chua chu cai thuong.")
#     if s.isupper():
#         print("Chuoi ban vua nhap chi chua chu cai hoa.")
#     if s.isspace():
#         print("Chuoi ban vua nhap chi chua ky tu trang.")
#     if s.isprintable:
#         print("Chuoi ban vua nhap chua ky tu dac biet.")
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
