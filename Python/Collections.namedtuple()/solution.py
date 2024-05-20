from collections import namedtuple

add = 0
N = input()
Student = namedtuple('Student',input().split())
#print(Student)
for i in range(0,int(N)):
    s= input().split()
    #print(*s)
    stds = Student(*s)
    #print(stds.MARKS)
    add+=int(stds.MARKS)
    
    
print("{:.2f}".format(add/int(N)))