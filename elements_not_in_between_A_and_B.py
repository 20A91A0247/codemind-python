n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
found = 0
for i in l:
    if i < a or i > b:
        found = 1
        print(i, end = ' ')
if found == 0:
    print(-1)