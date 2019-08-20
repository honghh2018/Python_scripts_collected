#encoding:utf-8
#!/usr/bin/env python
import re,sys,os
import time

BaseCounts = {}
with open(sys.argv[1]) as IN:
    for line in IN:
	if line.startswith(">"):
		line=line.replace('\n','').rstrip().strip('>')
		temp=line.split()
		BaseCounts[temp[0]]=''
	else:
		line=line.replace('\n','').rstrip('\n')
		BaseCounts[temp[0]] +=line.upper()

sys.stdout.write('Gene_ID\t'+'A\t'+'C\t'+'G\t'+'T'+'\t'+'N'+'\n')
for key in sorted(BaseCounts.keys()):
	ntCounts=[]
	for nt in ('A','C','G','T','N'):
    		ntCounts.append(BaseCounts[key].count(nt))
	mystr='\t'.join(map(str, ntCount))
	sys.stdout.write(key+'\t'+mystr+'\n')
