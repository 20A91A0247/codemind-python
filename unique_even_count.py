n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if(i%2==0):
        a.append(i)
ss=set(a)
s=list(ss)
print(len(s))