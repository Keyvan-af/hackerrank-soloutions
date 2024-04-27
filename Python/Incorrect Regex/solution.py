import re

no = int(input())
for _ in range(no):
    try:
        regex = input()
        if '*+' in regex or '++' in regex or '+?' in regex:
            print("False")
        else:
            re.compile(regex)
            print("True")
    except re.error:
        print("False")