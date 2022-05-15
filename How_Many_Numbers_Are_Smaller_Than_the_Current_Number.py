n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
for i in range(s):
    c=0
    for j in range(s):
        if(arr[i]>arr[j] and i!=j):
            c+=1
    print(c,end=" ")