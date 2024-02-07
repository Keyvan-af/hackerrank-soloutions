def print_rangoli(size):
    # your code goes here
    rangoli = []
    for i in range(size-1, -1, -1):
        line = []
        for j in range(size, i, -1):
            line.append(chr(96+j))
        line.extend(line[::-1][1:])
        rangoli.append(line)
    rangoli.extend(rangoli[::-1][1:])
    
    for line in rangoli:
        print("-".join(line).center((size*4)-3, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)