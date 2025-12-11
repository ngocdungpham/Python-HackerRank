def swap_case(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)