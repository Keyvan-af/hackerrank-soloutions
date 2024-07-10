K = int(input())
members = list(map(int, input().split(" ")))

from collections import Counter

members_count = Counter(members)

L = set(members_count.values())

result_1 = []
result_2 = []

for key, value in members_count.items():
    if value == list(L)[0]:
        result_1.append(key)
    else:
        result_2.append(key)

mini = min(len(result_1), len(result_2))
if len(result_1) == mini:
    print(result_1[0])
else: 
    print(result_2[0])
        