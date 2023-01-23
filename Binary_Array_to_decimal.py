n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
f=0
for i in range(n):
    f=f+(l[i]*(2**i))
print(f)