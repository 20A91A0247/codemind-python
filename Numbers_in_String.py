n=input()
l=[i for i in n]
j=0
for i in l:
    if(i.isdigit()):
        j=j+int(i)
print(j)