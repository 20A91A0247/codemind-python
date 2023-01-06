n=input()
l=[i for i in n]
j=0
z=0
for i in l:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='O'):
        j=j+1
for i in l:
    if(i.isdigit()):
        z=z+1
#print(z)
jj=n.count(" ")
#print(jj)
kk=len(n)
kkk=j+jj+z
q=kk-kkk
print("Vowels: {}".format(j))
print("Consonants: {}".format(q))
print("Digits: {}".format(z))
print("White spaces: {}".format(jj))