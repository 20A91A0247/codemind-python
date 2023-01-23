#element and count(level-17)
n=int(input())
ll=list(map(int,input().split()))
if(n%2!=0):
    ll.append(0)
    for i in ll:
        print(i,end=" ")
else:
    for i in ll:
        print(i,end=" ")