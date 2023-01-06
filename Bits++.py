t=int(input())
j=0
for i in range(t):
    n=input()
    if(n =='x++'or n =='++x'or n =='++X'or n =='X++'):
        j=j+1
    elif(n =='x--'or n =='--x'or n =='--X'or n =='X--'):
        j=j-1
    else:
        j=j-1
print(j)