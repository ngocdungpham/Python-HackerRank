import textwrap

def wrap(string, max_width):
    wrap_verst = textwrap.fill(string, max_width) # return string
    # wrap_verst = textwrap.wrap(string, max_width) # return list
    # print(textwrap.fill(string, max_width))
    return wrap_verst

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)