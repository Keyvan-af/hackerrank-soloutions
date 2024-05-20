# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

ordered_dict = OrderedDict()

for i in range(int(input())):
    
    input_string = input().split(' ')
    
    key = ' '.join(input_string[:-1])
    value = int(input_string[-1])
    
    if key not in ordered_dict:
        ordered_dict[key] = value
    
    else:
        ordered_dict[key] = ordered_dict[key] + value
    
    
for key,value in ordered_dict.items():
    
    print(key,value)
