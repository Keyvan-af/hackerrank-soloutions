# Enter your code here. Read input from STDIN. Print output to STDOUT
n_E = int(input())
set_E = set(map(int, input().split()))
n_F = int(input())
set_F = set(map(int, input().split()))
n_E_S = []
n_F_S = []

for idx, s in enumerate(set_F):
    n_F_S.append(s)

for idx, s in enumerate(set_E):
    n_E_S.append(s)
n_E_S = set(n_E_S)
n_F_S = set(n_F_S)
print(len(n_E_S.union(n_F_S)))