n=int(input())
temp=n
fact=1
s=0
i=1
while(n):
    fact=1
    d=n%10
    for i in range(1,d+1):
        fact=fact*i
    s=s+fact
    n=n//10
if(s==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")
        
    

    