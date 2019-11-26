def inc_dec(v,n):
    inc,dec=[1]*n, [1]*n
    fir_i,fir_d=[],[]
    for i in range(n):
        fir_i.append(i)
        fir_d.append(i)
    for j in range (1,n):
        for k in range(j):
            if v[j]>v[k] and inc[j]<=inc[k]:
                inc[j]=inc[j]+1
                fir_i[j]=k
            if v[j]<v[k] and dec[j]<=dec[k]:
                dec[j]=dec[j]+1
                fir_d[j]=k
    max_i,max_d=max(inc),max(dec)
    index_i,index_d=inc.index(max_i), dec.index(max_d)
    inc,dec=[v[index_i]], [v[index_d]]
    while index_i != fir_i[index_i]:
        index_i=fir_i[index_i]
        inc.append(v[index_i])
    while index_d != fir_d[index_d]:
        index_d=fir_d[index_d]
        dec.append(v[index_d])
    return inc[::-1], dec[::-1]

with open ('rosalind_lgis.txt') as f:
    n=int(f.readline().strip())
    pi=list(map(int,f.readline().split()))
 

inc,dec=inc_dec(pi,n)
print (*inc)
print(*dec)    