n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if i not in e:
        e.append(i)
print(*e)