for _ in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    i = 0
    valid = True
    while (i < max(n//2-1, 1) and valid):
        l_most, l, r_most, r = arr[i], arr[i+1], arr[-1-i], arr[-2-i]
        valid = (l <= l_most or l <= r_most) and (r <= l_most or r <= r_most)
        i += 1
    print('Yes' if valid else 'No')