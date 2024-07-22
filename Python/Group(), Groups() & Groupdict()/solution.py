import re

if __name__=="__main__":
    s = input()
    r = re.search(r'([0-9a-zA-Z]{1})\1+',s)
    if r:
        print(r.group(0)[0])
    else:
        print(-1)