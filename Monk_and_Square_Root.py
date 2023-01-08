n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    k=[]
    for i in range(a+b):
        if (i*i)%b==a:
            k.append(i)
    if(k==[]):
        print(-1)
    else:
        print(min(k))