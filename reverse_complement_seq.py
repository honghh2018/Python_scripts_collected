
def rev_com(seq):  #defined function and use parameter as input
    nt_rev_com={'A':'T','C':'G','T':'A','G':'C'} #dictionary
    rev_seq_list=list(reversed(seq))
    revcomlist = [nt_rev_com[k] for k in rev_seq_list]  #loop
    revcom=''.join(revcomlist)
    return(print(revcom))  #return the function value

seq="ATCG"
rev_com(seq) #invoking the function rev_com
