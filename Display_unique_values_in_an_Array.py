n=int(input())
a=list(map(int,input().strip().split()))
b=[]
for i in a:
    if i not in b and a.count(i)==1:
        b.append(i)
if b==[]:
    print("-1")
else:
    print(*b)
       