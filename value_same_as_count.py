#value same as count
n=int(input())
l=list(map(int,input().split()))
a=[]
f=0
for i in l:
    if(i==l.count(i)):
        f=f+1
        a.append(i) 
ll=set(a)
mm=list(ll)
mm.sort()
if(f>0):
    print(len(mm))
else:
    print(0)