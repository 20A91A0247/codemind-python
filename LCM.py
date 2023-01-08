n,m=map(int,input().split())
k=[]
kk=[]
for i in range(1,n+30):
    f=n*i
    k.append(f)
for i in range(1,m+30):
    f=m*i
    kk.append(f)
v=[]
for i in k:
    if i in kk:
        v.append(i)
print(min(v))