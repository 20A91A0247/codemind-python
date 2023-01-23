import math
n=int(input())
l=list(map(int,input().split()))
z=int(sum(l)/n)
j=0
for i in l:
    if(i<=z):
        j+=1
print(j)