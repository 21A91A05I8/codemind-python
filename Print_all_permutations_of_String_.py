from itertools import permutations
s=input()
w=[''.join(p) for p in permutations(s)]
for i in w:
    print(i)