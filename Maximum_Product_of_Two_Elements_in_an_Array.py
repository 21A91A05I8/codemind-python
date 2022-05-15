arr=list(map(int,input().split()))
s=len(arr)
max=0
k=0
for i in range(s):
    for j in range(i+1,s):
        k=(arr[i]-1)*(arr[j]-1)
        if(k>max):
            max=k
print(max)
        