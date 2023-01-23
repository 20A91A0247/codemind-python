n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
l2=[]
for j in l1:
    c=l.count(j)
    l2.append(c)
for i in range(len(l1)):
    print(l1[i],l2[i],end=' ')