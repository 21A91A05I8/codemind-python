n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
k=0
c=0
for i in range(s):
    if(arr[i]!=0):
        arr[c]=arr[i]
        c+=1
for i in range(c,n):
    arr[i]=0
for i in range(s):
    print(arr[i],end=" ")