from collections import deque


if __name__ == '__main__':
    dq = deque()
    operations = {
        'append': dq.append,
        'appendleft': dq.appendleft,
        'pop': dq.pop,
        'popleft': dq.popleft
    }
    n = int(input().rstrip())
    for i in range(n):
        line = input().rstrip().split()
        if len(line) == 1:
            operations[line[0]]()
        else:
            operations[line[0]](line[1])
    print(*dq)