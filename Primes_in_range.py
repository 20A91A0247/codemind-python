from math import *
def isp(n):
    if n<=1:
        return 0
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return 0
        else:
            return 1
n=int(input())
n1=int(input())
s=0
for i in range(n,n1+1):
    s=s+isp(i)
print(s)