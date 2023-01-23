n=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if(i==0 or i==1):
        f=f+1
if(f==n):
    print("True")
else:
    print("False")