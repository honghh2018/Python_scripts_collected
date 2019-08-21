#encoding:utf-8
#!/usr/bin/env python
import os,sys,re
#sys.setdefaultencoding('utf-8')


stat1=dict() #defining global variable 
#global dict(stat1)
fr=open(sys.argv[1])

def readfile(handle):
        global stat1 #garnered global variable authority stat1
        for line in handle:
                line=line.replace('\n','').rstrip()
                if line.startswith('#'):
                        continue
                temp=line.split('\t')
                if temp[0] not in stat1:
                        #stat1[temp[0]]=0
                        stat1.setdefault(temp[0],0)
                stat1[temp[0]] +=1 #achieving dictionary +=1

readfile(fr)
fr.close()
for key,value in sorted(stat1.items(),key=lambda x:x[1],reverse=True): #stat1.items() returning key and value;x:x[0] sorted by key,
                                                                       #x:x[1] sorted by value
        print(str(key)+':'+str(value)) 
