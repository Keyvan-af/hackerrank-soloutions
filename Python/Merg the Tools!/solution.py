def merge_the_tools(string, k):
    sb = ''
    for idx, s in enumerate(string, start=1):
        if s not in sb:
            sb = sb + s
        if idx % k == 0:
            print(sb)
            sb = ''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)