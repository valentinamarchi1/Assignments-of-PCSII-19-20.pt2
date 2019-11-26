from itertools import product

def lexf(seq,n):
    for perm in product(a, repeat=n): 
        print( "".join(perm))

with open('rosalind_lexf.txt') as f:
    a = list(f.readline().rstrip().split())
    n = int(f.readline().rstrip())

print(lexf(a,n))