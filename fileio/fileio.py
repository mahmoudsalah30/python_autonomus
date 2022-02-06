from anyio import open_file


f=open('inputfile.txt','r')
pass_file=open('pass_file.txt','w')
fail_file=open('fail_file.txt','w')
for  line in f :
     line_split=line.split()
     if line_split[2] =='p':
          pass_file.write(line)
     else :
          fail_file.write(line) 
f.close()
pass_file.close()
fail_file.close()             