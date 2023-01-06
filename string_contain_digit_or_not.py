n=input()
l=[i for i in n]
j=0
for i in l:
    if(i.isdigit()):  
        j=j+1
if(j==0):
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(j))