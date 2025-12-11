def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    string_length = len(string)

    for i in range(string_length):
        if string[i] in vowels:
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i
        print(f"Index: {i}, Char: {string[i]}, Kevin Score: {kevin_score}, Stuart Score: {stuart_score}")
        

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)