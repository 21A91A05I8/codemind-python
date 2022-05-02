n=int(input())
s=0
mul=1
while(n):
    d=n%10
    s=s+d
    mul=mul*d
    n=n//10
diff=mul-s
print(diff)
    