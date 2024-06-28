from collections import Counter

num_words = int(input())
words = []
for i in range(num_words):
    word = input()
    words.append(word)
    
print(len(set(words)))

string_counted = Counter(words)
counts = []
for string, count in string_counted.items():
    counts.append(str(count))
    
print(' '.join(counts))
