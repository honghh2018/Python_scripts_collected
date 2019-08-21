#!/usr/bin/env python
import os,sys,re

with open(sys.argv[1]) as IN:
        for line in IN:
                line=line.replace('\n','').rstrip()
                if line.startswith('#'):
                        print(line)
                        continue
                temp=line.split('\t')
                sys.stderr.write(str(len(temp))+'\n')
                if len(temp)==1:
                        continue
                newtemp=['0' if i=='' else i for i in temp] #replacing list element for certain conditions by list expression 
                mystr='\t'.join(newtemp)
                print(mystr)
