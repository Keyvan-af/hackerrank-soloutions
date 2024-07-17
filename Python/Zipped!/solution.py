N, X = map(int, input().split(" "))
lists = []

for i in range(X):
    A = list(map(float, input().split(" ")))
    lists.append(A)
    
summed_elements = [sum(elements)/X for elements in zip(*lists)]
for nums in summed_elements:
    print(nums)

