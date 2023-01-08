n=int(input())
temp=n
l=[]
while n:
    r=n%10
    s=1
    n=n//10
    for i in range(r,0,-1):
        s*=i
    l.append(s)
if sum(l)==temp:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")