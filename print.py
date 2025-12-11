if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum = a + b
    sub = a - b
    product = a * b
    print(sum)
    print(sub)
    print(product)
    a, b = 3, 2
    print(f"Tổng: {a+b}, Hiệu: {a-b}, Tích: {a*b}")
    a, b = 4, 5
    print("Tổng: {}, Hiệu: {}, Tích: {}".format(a+b, a-b, a*b))
    a, b = 3, 2
    print("Tổng: %d, Hiệu: %d, Tích: %d" % (a+b, a-b, a*b))
    a, b = 10, 11
    print(a+b, a-b, a*b)



