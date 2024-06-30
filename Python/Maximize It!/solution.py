from itertools import product

k, m = map(int, input().split())

combinations = [list(map(int, input().split()))[1:] for _ in range(k)]
print(max([sum([x**2 for x in item]) % m for item in product(*combinations)]))