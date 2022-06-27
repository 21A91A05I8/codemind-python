n=int(input())
s=list(map(int,input().split()))
d=int(input())
c=0
for i in range(len(s)):
    if(i==d):
        break
    else:
        c=c+s[i]
print(c)