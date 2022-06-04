n=input()
c=0
for i in range (len(n)):
    if n[i]!=' ':
        c+=1
    if(n[i]==' '):
        break
print(c)
