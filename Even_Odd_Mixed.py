n=int(input())
even=0
odd=0
while(n>0):
    d=n%10
    n=n//10
    if(d%2==0):
        even+=1
    if(d%2!=0):
        odd+=1
if(even!=0 and odd!=0):
    print("Mixed")
elif(odd==0):
    print("Even")
else:
    print("Odd")
        
    
        