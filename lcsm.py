def lcsm(strands):
    strand1=strands[1]
    k=''
    res=''
    for i in range (len(strand1)):
        for j in range (i+1, len(strand1)+1):
            k=strand1[i:j]
            for h in range(1, len(strands)):
                if k not in strands[h]:
                    break
                if h + 1 == len(strands) and len(res) < len(k):
                    res=k
    return res       

with open('rosalind_lcsm.txt') as f:
    A=f.read().split('>Rosalind_')
    l=[]
    for g in A:
        g=g.strip()
        g=g.replace('\n', '')
        l.append(g)  
        
with open('rosalind_lcsm_out.txt', 'w') as f:
    f.write(lcsm(l))