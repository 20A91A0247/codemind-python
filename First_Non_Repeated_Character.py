t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    #print(n,s)
    k=[]
    for j in s:
        if s.count(j)==1:
            k.append(j)
    if k==[]:
        print(-1)
    else:
        print(k[0])