import shutil
f1=open("must1.txt",mode='r')
f2=open("must2.txt",mode='w')
f2.write(f1.read())
shutil.copyfile("must1.txt","must2.txt")
f1.close()
f2.close()
