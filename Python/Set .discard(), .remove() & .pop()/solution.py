n = int(input())
s = set(map(int, input().split()))

size = int(input())

for _ in range(size):
    operation = input().split()
    expression = ''
    if len(operation) < 2:
        expression = 's.'+operation[0]+'()'
    else:
        expression = 's.'+operation[0]+'('+operation[1]+')'
    eval(expression)

print(sum(s))
