A,B,C=map(int,input().split())
s=(A+B+C)/2
a=(s*(s-A)*(s-B)*(s-C))**0.5
print('{:.2f}'.format(a))
