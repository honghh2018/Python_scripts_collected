#!/usr/bin/env python
import sys,os,re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

fw=open(sys.argv[2],"w")
fw.write('Gene_ID\t'+'A(bases)\t'+'C(bases)\t'+'G(bases)\t'+'T(bases)'+'\t'+'N(bases)'+'\t'+'N_percentage(%)''\n')
biggestN={}
recordall={}
with open(sys.argv[1]) as IN:
        for seq_record in SeqIO.parse(IN, "fasta"):
                #print('>'+seq_record.id+' '+str(len(seq_record)))
                #print(str(seq_record.seq))
                #SeqIO.write(seq_record, fw, "fasta")
                Tempcount=[]
                #print(seq_record.seq.upper().count('A'))
                for nt in ('A','T','C','G','N'):
                        Tempcount.append(seq_record.seq.upper().count(nt))
                totallength=len(seq_record.seq)
                N_percentage=round((Tempcount[-1]/int(totallength))*100.0,2)
                Tempcount.append(N_percentage)
                line='\t'.join(map(str, Tempcount))
                result_count=seq_record.id+'\t'+line
                biggestN[seq_record.id]=Tempcount[-2]
                recordall[seq_record.id]=result_count
        for key,value in sorted(biggestN.items(),key=lambda x:x[1],reverse=True):
                if key in recordall.keys():
                        print >>fw,"{}".format(recordall[key])
fw.close()
'''
record = SeqIO.read(sys.argv[1], "fasta")
print('>'+record.id)
print(record.seq)
