#encoding:utf-8
#!/usr/bin/env python 
import os,sys,re

infile_list=[]
abs_path=os.path.abspath(sys.argv[1])

for file in os.listdir(abs_path):
        file=file.replace('\n','').strip()
        mypath=abs_path+'/'+file
        infile_list.append(mypath)

print("#Sample_ID\tPercentage(%)")
fw=open('out.xls','w')
for i in sorted(infile_list):
        match1=re.search(r'.*-(L\d{2})\.sam',i,re.M|re.I)
        if match1:
                with open(i) as IN:
                        count=0
                        count1=0
                        for line in IN:
                                line=line.replace('\n','').strip()
                                if line.startswith('@'):
                                        continue
                                temp=line.split('\t',5)
                                count+=1
                                #sys.stderr.write("mark:"+temp[0]+'\n')
                                if temp[2]=='NC_008602.1_chloroplast':
                                        count1 +=1
                        count2=count/2.0
                        sys.stderr.write("all count: "+str(count2)+'\n')
                        target=count1/2.0
                        sys.stderr.write("mark: "+str(target)+'\n')
                        target1 = round((target/count2)*100.0,2)
                        print("{0}\t{1}".format(match1.group(1),target1))
                        sys.stdout.flush() #刷新标准刷输出缓冲区
                        fw.flush() #刷新文件输出缓冲区
