l,r,k=map(int,input().split())
fc=0
for i in range(l,r+1):
    if i%k==0:
        fc+=1
print(fc)