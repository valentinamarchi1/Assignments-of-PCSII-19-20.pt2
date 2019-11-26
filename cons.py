def read_FASTA(f):
    sequences=[]
    keys=[]
    temp_arr=[]
    for line in open(f , "r"):
        if line[0]!=">":

            if len(line)>59:
                temp_arr.append(line[:-1])
                
            elif len(line)<59:
                temp_arr.append(line[:-1])
                sequences.append( "".join(temp_arr) )
                temp_arr=[]
                
        else:
            keys.append(line[1:-1])
            
            
    return sequences


strand=read_FASTA("rosalind_cons.txt")
lon=len(strand[0])
nA=[0]*lon ; nT=[0]*lon ; nG=[0]*lon ; nC=[0]*lon 

for i in strand:
    ls=list(i)
    c=0
    while c<lon:
        if i[0+c]=="A":
            nA[0+c]+=1
            c+=1
        elif i[0+c]=="C":
            nC[0+c]+=1
            c+=1
        elif i[0+c]=="G":
            nG[0+c]+=1
            c+=1
        elif i[0+c]=="T":
            nT[0+c]+=1
            c+=1

cons="" 
for i in range(lon):
    if nA[0+i]>=nC[0+i] and nA[0+i]>=nG[0+i] and nA[0+i]>=nT[0+i]:
        cons+="A"
    elif nC[0+i]>=nA[0+i] and nC[0+i]>=nG[0+i] and nC[0+i]>=nT[0+i]:
        cons+="C"
    elif nG[0+i]>=nA[0+i] and nG[0+i]>=nC[0+i] and nG[0+i]>=nT[0+i]:
        cons+="G"
    elif nT[0+i]>=nA[0+i] and nT[0+i]>=nG[0+i] and nT[0+i]>=nC[0+i]:
        cons+="T"
            
print(cons)

print("A: {}".format( " ".join(list(map(str , nA)))) )
print("C: {}".format( " ".join(list(map(str , nC)))) )
print("G: {}".format( " ".join(list(map(str , nG)))) )
print("T: {}".format( " ".join(list(map(str , nT)))) )