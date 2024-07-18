import re
t = int(input())
for _ in range(t):
    print(bool(re.search(r'^[+-]?[0-9]*\.[0-9]+$', input())))