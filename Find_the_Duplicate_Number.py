n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
c=1
for i in range(s):
    c=1
    for j in range(s):
        if(arr[i]==arr[j] and i!=j):
            k=arr[i]
print(k)
            

            