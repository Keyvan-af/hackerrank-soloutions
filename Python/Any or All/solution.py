num = int(input())
nums = list(map(int, input().split(" ")))
print(all([_ > 0 for _ in nums]) and any([str(num) == str(num)[::-1] for num in nums]))
