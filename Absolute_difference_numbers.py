a,b=map(str,input().split())
m=int(a[:int(b)])
n=int(a[-int(b):])
print(abs(m-n))