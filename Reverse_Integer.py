n=int(input())
t=n
if(n<0):
    n=abs(n)
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(t>0):
    print(rev)
else:
    print(-rev)

