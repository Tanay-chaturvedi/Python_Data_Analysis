# a="harry is good"
# file=open("harry.txt","w")#opening a file name harry in write mode
# file.write(a)
# file.close()
# ---------------------------------

# r=read Mode 
# w=write Mode 
# a=append mode 
# x=create file 
# rb=read binary 
# wb=write binary 
# file=open("robot.txt","r")# to see output first we need to create a file named robot or whatever ypu ean to give
# # content=file.read()
# content=file.readlines()#output will no longer be a string it will be in list format
# print(content)
# file.close()
# --------------------------

#for append
# a="\n I am also good"
# file=open("robot.txt","a")
# file.write(a)
# file.close() #see outout in robot.txt a new line will be added
#--------------------------------------------------------------------------
a="\n I am also good"
with open("robot.txt","a") as f:
    f.write(a)  #no need to close file here it will auotmatically use it