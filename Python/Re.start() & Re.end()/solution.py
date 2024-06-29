import re

s = input()
k = input()

pattern = re.compile(f'(?=({k}))')
result = list(pattern.finditer(s))

for match in result:
    print((match.start(1), match.end(1)-1))
if k not in s:
    print((-1,-1))