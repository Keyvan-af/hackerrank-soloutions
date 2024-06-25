from itertools import groupby
s = input()

for k, i in groupby(s):
    print((list(i).count(k), int(k)), end=' ')

    