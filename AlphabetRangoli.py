import string
def print_rangoli(size):
    list = []
    for i in range(2 * size - 1):
        if i < size:
            list.append(string.ascii_lowercase[size-1-i])
            a = '-'.join(list)
            b = a[::-1]
            r = a + b[1:]
            print(r.center(4*size-3, '-'))
        else: 
            list.pop()
            a = '-'.join(list)
            b = a[::-1]
            r = a + b[1:]
            print(r.center(4*size-3,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)