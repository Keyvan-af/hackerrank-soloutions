def average(array):
    non_dup = set(array)
    counter = len(non_dup)
    sum_set = sum(list(non_dup))
    return round(sum_set/counter, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)