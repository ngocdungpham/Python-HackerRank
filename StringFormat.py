from asyncio import log
import math
def print_formatted(number):
    # your code goes here
    c = int(math.log2(number)) + 1
    for i in range(number):
        decimal = str(i + 1)
        octal = oct(i + 1)[2:]
        hexadecimal = hex((i + 1))[2:].upper()
        binary = bin(i + 1)[2:]
        print(decimal.rjust(c, ' '), end=' ')
        print(octal.rjust(c, ' '), end=' ')
        print(hexadecimal.rjust(c, ' '), end=' ')
        print(binary.rjust(c, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)