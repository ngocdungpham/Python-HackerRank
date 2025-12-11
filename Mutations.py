"""
string = "abracadabra"
l = list(string)
l[5] = "k"
string = ''.join(l)
print(string)
string = string[:5] + "k" + string[6:]
print(string)
print(string[:5])
print(string[6:])
"""

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

