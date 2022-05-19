n=int(input())
for i in range(0,n):
    t=int(input())
    temp=t
    rev=0
    while(t>0):
        d=t%10
        rev=rev*10+d
        t=t//10
    if(temp==rev):
        print("True")
    else:
        print("False")