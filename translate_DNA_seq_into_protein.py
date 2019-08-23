#!/usr/bin/env python
import sys,os,re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
'''
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
'''
fasta_dict = SeqIO.to_dict(SeqIO.parse(sys.argv[1], "fasta")) #read fasta file and turn into dictionary struture

#for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
#    print(seq_record.id)
#    print(repr(seq_record.seq))
#    print(len(seq_record))

for key in sorted(fasta_dict.keys(),key=lambda x:x[0],reverse=True):
        #print('value:'+str(orchid_dict[key].seq))  #Wraper value have four methods listing id,seq,description,name 
        #sys.stderr.write('value:'+str(type(key))+'\n') 
        coding_dna=Seq(str(fasta_dict[key].seq), IUPAC.unambiguous_dna)  #the input sequence must be string not a object,then str need to call
        print ">{}\n{}".format(key,coding_dna.translate())
