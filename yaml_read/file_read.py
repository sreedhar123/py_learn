from sys import argv
script_name, file_name=argv
print "the file name is %s" %file_name
f1=open(file_name)
txt=f1.read()
print txt
