A = set(map(int, input().split(" ")))

N = int(input())
list_sets = []
for i in range(N): 
    L = set(map(int, input().split(" ")))
    list_sets.append(L)
    
boolean = []    
for s in list_sets:
    if s == A:
        boolean.append("False")
    elif s.issubset(A):
        boolean.append("True")
    else:
        boolean.append("False")
if "False" in boolean:
    print("False")
else:
    print("True")
    
    