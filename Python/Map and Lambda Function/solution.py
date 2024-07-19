cube = lambda x: x**3

def fibonacci(n):
    list_fib = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    else:
        
        for i in range(2, n):
            list_fib.append(list_fib[i-1] + list_fib[i-2])

        return list_fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))