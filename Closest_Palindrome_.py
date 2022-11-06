n=int(input())
a=n+1
b=n-1
while True:
    rev=0
    t1=a
    while a>0:
        rem=a%10
        rev=rev*10+rem
        a=a//10
    if(rev==t1):
        break
    else:
        a=t1+1
while True:
    rev=0
    t2=b
    while b>0:
        rem=b%10
        rev=rev*10+rem
        b=b//10
    if(rev==t2):
        break
    else:
        b=t2-1
if abs(t1-n)>abs(n-t2):
    print(t2)
elif abs(t1-n)<abs(n-t2):
    print(t1)
elif abs(t1-n)==abs(n-t2):
    print("{} {}".format(t2,t1))