a,b=map(int,input().split())
c=a
d=b
while(a!=0 and b!=0):
    if a>b:
        a=a%b
    else:
        b=b%a
p=max(a,b)
print((c*d)//p)