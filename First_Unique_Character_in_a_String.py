s=input()
k=-1
for i in s:
    if s.count(i)==1:
        k=s.index(i)
        break
if(k>=0):
    print(k)
else:
    print(k)