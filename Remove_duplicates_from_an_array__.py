n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
for i in range(s):
    for j in range(s):
        if(arr[i]==arr[j] and i!=j):
            arr[j]=-100
    if(arr[i]!=-100):
        print(arr[i],end=" ")
