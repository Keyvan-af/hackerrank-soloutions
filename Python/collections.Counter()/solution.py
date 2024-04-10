from collections import Counter
num_shoes = int(input())
list_shoes = input()
list_s = [x for x in list_shoes.split()]
customers = int(input())
counts = Counter(list_s)
somma = 0
for i in range(customers):
    prod_i = input()
    size_i = prod_i.split()[0]
    price_i = int(prod_i.split()[1])
    if size_i in counts.keys() and counts[size_i] > 0:
        somma += price_i
        counts[size_i] -= 1
print(somma)