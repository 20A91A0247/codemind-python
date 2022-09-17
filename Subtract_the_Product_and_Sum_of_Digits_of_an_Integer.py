n=int(input())
i=1
s=0
p=1
while i <n:
    r=n%10
    n=n//10
    p=p*r
    s+=r
print(p-s)