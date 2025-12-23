def find_needle(haystack):
    return f"found the needle at position {haystack.index("needle")}"

def string_to_array(s):
    return s.split()

if __name__ == '__main__':
    haystack = input().split()
    print(find_needle(haystack))