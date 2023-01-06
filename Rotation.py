t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(k):
        z=l.pop()
        l.insert(0,z)
    print(*l )