n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
ec=0
oc=0
for i in range(s):
    if(arr[i]%2==0):
        ec+=1
    else:
        oc+=1
print(ec,oc,end=" ")