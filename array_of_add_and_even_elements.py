n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
z=[]
z.extend(o)
z.extend(e)
for i in z:
    print(i,end=" ")