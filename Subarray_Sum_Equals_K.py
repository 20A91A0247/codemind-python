a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(i,len(l)):
        kk=[]
        for k in range(i,j+1):
            kk.append(l[k])
        if sum(kk)==b:
            c=c+1
print(c)