n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
su=0
k=0
for i in range(s):
    if(i%2==0):
        su=su+arr[i]
    else:
        k=k+arr[i]
if(su==k):
    print("YES")
else:
    print("NO")
        