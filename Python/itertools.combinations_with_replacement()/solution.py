from itertools import combinations_with_replacement

st, num = input().split(" ")
list_iter = list(combinations_with_replacement(sorted(st), int(num)))

for i in range(len(list_iter)):
    print(''.join(list_iter[i]))
