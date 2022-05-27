n=int(input())
a=list(map(int,input().split()))
max=0
for i in range(len(a)):
    k=a.count(a[i])
    if(k>max):
        max=k
        m=a[i]
print(m)