#!/usr/bin/env python 
import os,sys,re
import glob    #like perl glob

result=os.getenv('PATH') #get current system environmental path
#print(result)
abs_path=os.path.abspath(sys.argv[1])
#sumfile=abs_path+'/'+'*.gz'
myfile=glob.glob(abs_path+'/'+'*.gz') #same worked
#myfile=glob.glob(sumfile) #all same
for i in sorted(myfile):
        result1=os.path.split(i)
        print "directory:{}\tgeneral file:{}".format(result1[0],result1[1]) #directory:/home/hui/gz_data        general file:sample1.fq.gz
        #print "mark:%s"%i
