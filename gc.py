def gc(strand):
    counter=0
    for i in strand:
        if i.lower() in 'gc':
            counter+=1
    return counter /len(strand)

import os 

def file_reader(file_name,fasta=False):
    to_split_at="\n"
    if fasta:
        to_split_at=">"
    path=os.path.expanduser("~/desktop/"+ file_name)
    with open(path,"r") as file:
        s=file.read()
    return s.split(to_split_at)[:-1]


if __name__ =='__main__':
    input_list=file_reader("rosalind_gc.txt", fasta=True)[1:]
    best_fasta= None
    best_count= 0
    for i in range(len(input_list)):
        input_sublist=input_list[i].split("\n")
        fasta_name=input_sublist[0]
        fasta_code="".join(input_sublist[1:])
        c=gc(fasta_code)
        if c> best_count:
            best_fasta=fasta_name
            best_count=c
    print(best_fasta)
    print(best_count*100)
    
