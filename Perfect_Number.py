n=int(input())
def isperfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
print(isperfect(n))