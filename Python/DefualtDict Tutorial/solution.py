from collections import defaultdict

n, m = [int(num) for num in input().split(' ')]


d = defaultdict(list)
for i in range(n):
    word = input()
    d[word].append(i)
    
for _ in range(m):
    word = input()
    if not d[word]:
        print('-1')
        continue
    print(' '.join(str(num + 1) for num in d[word]))