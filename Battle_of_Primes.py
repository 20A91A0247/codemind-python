n=int(input())
m=int(input())
k=[]
s=n+m
for i in range(1,s+10):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            k.append(i)
for i in k:
    if i>s:
        print(i-s)
        break