n = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in arr:
    if i in A:
        happiness = happiness+1
    elif i in B:
        happiness = happiness-1
    else:
        pass
print(happiness)