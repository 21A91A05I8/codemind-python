import math
n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
c=0
dc=0
for i in range(s):
    c=0
    while(arr[i]):
        d=arr[i]%10
        c+=1
        arr[i]=arr[i]//10
    if(c%2==0):
        dc+=1
print(dc)
    
    
       