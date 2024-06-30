n_E = int(input())
L_E = input().split(" ")
n_F = int(input())
L_F = input().split(" ")
L_E = [int(num) for num in L_E]
L_F = [int(num) for num in L_F]

print(len(set(L_E) ^ set(L_F)))