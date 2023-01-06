n=input()
j=0
for i in n:
    if(i.isupper()):
        j=j+1
if n[0].isupper():
    print(j)
else:
    print(j + 1)