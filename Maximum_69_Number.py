n=input()
k=[]
for i in n:
    k.append(int(i))
for i in range(len(k)):
    if k[i]==6:
        k[i]=k[i]+3
        break
for i in k:
    print(i,end="")