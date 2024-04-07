from itertools import combinations
S, k = input().split(' ')
sorted_S = ''.join(sorted(S))
for m in range(1, int(k)+1):
    x = combinations(str(sorted_S), m)
   
    for i in x:
        print(''.join(i))