# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
mid=n//2
des='.|.'
cnt=1
for i in range(n):
    if i==mid:
        print('WELCOME'.center(m, '-'))
    else:
        print((des*cnt).center(m, '-'))
    if i<mid:
        cnt+=2
    else:
        cnt-=2
