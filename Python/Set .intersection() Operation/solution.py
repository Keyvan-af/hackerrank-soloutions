n = int(input())
E = set(map(int, input().split()))
b = int(input())
F = set(map(int, input().split()))

total = E.intersection(F)
print(len(total))