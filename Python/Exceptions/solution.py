T = int(input())
samples = []
for i in range(T):
    a, b = list(input().split())
    samples.append([a, b])

for j in samples:
    try:
        print(int(j[0]) // int(j[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        