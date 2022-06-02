n=int(input())
s=list(map(int,input().split()))
min=999
fo=0
for i in range(0,n):
    if(min>s[i]):
        min=s[i]
for i in range(min,0,-1):
    fo=0
    for j in range(0,n):
        if(s[j]%i!=0):
            fo=1
            break
    if(fo==0):
        print(i)
        break
            
    
