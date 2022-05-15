n=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
s=len(arr)
c=0
for i in range(n):
    c=arr[i]+brr[i]
    print(c,end=" ")