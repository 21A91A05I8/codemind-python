n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if(i%2==0):
        break
    else:
        c=c+i
print(c)