#unique elements(level-15)

n=int(input())
l=list(map(int,input().split()))
e=0
for i in l:
    if(i%2==0):
        e=e+1
if(e==n):
    print("True")
else:
    print("False")