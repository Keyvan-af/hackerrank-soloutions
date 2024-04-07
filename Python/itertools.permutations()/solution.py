from itertools import permutations
S, k = input().split(' ')
sorted_s = ''.join(sorted(S))
x = permutations(str(sorted_s), int(k))

for i in x:
    print(''.join(i))