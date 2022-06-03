n=input()
v=0
c=0
d=0
s=0
for i in n:
    if i in 'aeiou':
        v+=1
    if i not in 'aeiou0123456789 ':
        c+=1
    if i in '0123456789' :
        d+=1
    if i in' ':
        s+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)
    