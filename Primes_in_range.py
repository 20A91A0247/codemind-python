import math
def gr(a,b):
    c=0
    for i in range(a,b+1):
        if i>1:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                c=c+1
    print(c)
a=int(input())
b=int(input())
gr(a,b)