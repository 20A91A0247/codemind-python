n=int(input())
l=list(map(int,input().split()))
t=int(input())
k=[]
for i in l:
    if i+t>=max(l):
        k.append("True")
    else:
        k.append("False")
print(*k)