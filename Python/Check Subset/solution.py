T = int(input())
list_case = []
for i in range(T):
    N = int(input())
    A = set(map(int, input().split(" ")))
    M = int(input())
    B = set(map(int, input().split(" ")))
    
    list_case.append([A, B])

for i in list_case:
    print(i[0].issubset(i[1]))
