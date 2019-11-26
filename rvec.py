def revc(strand):
    revstrand=strand[::-1]
    revcomple=""
    
    for i in range(len(revstrand)):
        if revstrand[i]=='A':
            revcomple+='T'
        if revstrand[i]=='T':
            revcomple+='A'
        if revstrand[i]=='C':
            revcomple+='G'
        if revstrand[i]=='G':
            revcomple+='C'
            
    return revcomple