m, M, n, N = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split())) 
print(*sorted(M.symmetric_difference(N)), sep='\n')