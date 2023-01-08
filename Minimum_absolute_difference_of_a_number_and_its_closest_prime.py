n=int(input())
k=[]
for i in range(n-10,n+10):
    if(i>=1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            k.append(i)
z=[]
for i in k:
    z.append(abs(n-i))
print(min(z))