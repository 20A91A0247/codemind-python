n=int(input())
l=list(map(int,input().split()))
a=[]
j=0
for i in l:
    if(i%2!=0):
        a.append(i)
s=set(a)
ss=list(s)
ss.sort()
if(len(ss)!=0):
    print(len(ss))
else:
    print(0)