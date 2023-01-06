a=input()
m=int(input())
l=len(a)
if m%l==0:
    x=int(m//l)
    y=a.count("a")
    print(y*x)
else:
    x=int(m//l)
    y=l*x
    z=m-y
    ss=a[:z]
    h=ss.count("a")
    g=a.count("a")
    print(h+(g*x))