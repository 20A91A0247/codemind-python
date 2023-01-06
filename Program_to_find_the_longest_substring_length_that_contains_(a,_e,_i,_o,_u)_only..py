n=input()
v="aeiou"
c=0
k=[]
for i in n:
    if i in v:
        c=c+1
        k.append(c)
    else:
        c=c-c
print(max(k))