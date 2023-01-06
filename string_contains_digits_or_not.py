t=int(input())
for i in range(t):
    n=input()
    j=0
    l=[i for i in n]
    for i in l:
        if(i.isdigit()):
            j=j+1
    if(j!=0):
        print("Yes")
    else:
        print("No")