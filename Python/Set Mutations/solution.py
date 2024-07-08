N = int(input())
A = set(map(int, input().split(" ")))
Number_Operations = int(input())
list_Operations = []
list_sets = []
for i in range(Number_Operations):
    opo = input().split(" ")[0]
    B = set(map(int, input().split(" ")))
    list_Operations.append(opo)
    list_sets.append(B)

for index, operation in enumerate(list_Operations):
    if operation == "update":
        A.update(list_sets[index])
    elif operation == "intersection_update":
        A.intersection_update(list_sets[index])
    elif operation == "difference_update":
        A.difference_update(list_sets[index])
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(list_sets[index])
    else:
        pass

print(sum(A))