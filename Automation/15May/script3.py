from sys import *
import os
import hashlib
import schedule
import time 

def CalculateChecksum(path, blocksize = 1024): #positonal para, default para
    fd = open(path,'rb')#read in binary mode
    hobj = hashlib.md5() #md5 algo for hashing
    #if file size is 2051 bytes 
    buffer = fd.read(blocksize) #array
    while len(buffer) > 0:
        hobj.update(buffer) # data given in chunks for the algo which we are using md5
        buffer = fd.read(blocksize)# 2nd iteration ,after 1024 bytes  read the remaining will be read 

    fd.close()
    return hobj.hexdigest()
    
def DirectoryTraversal(path):
    
    print("Absolute path is ")
    abspath = os.path.abspath(path) #gives the output as C:\Users\akank\Desktop\Python\15May\Demo i.e the path of the folder given as input 
    print(abspath)
    print("Contents of the directory are")
    
    for Folder , Subfolder , Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:
            print("Subfolder of  " + Folder + "is "+ sub)
        for file in Filename:
            print("File name is : "+file)
            actualpath = os.path.join(Folder,file) #like concate
            
            hash = CalculateChecksum(actualpath)
            print(hash)

    File_Path = os.path.join("Log","Marvellous%s.log"%i)
    i = i+1
    print("file path")
   
    fd = open(File_Path,"w")
    print("file open")
    
    for code in hash:
        fd.write("%s\n"% code)       
    print("check sum written on file")

def main():
    print("Marvellous Infosystems")
    print("Directory travesal script")
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or  (argv[1] == "-H"):
        print("It is a Directory cleaner script")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Provide the absolute path of the target director")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(DirectoryTraversal)
        print("scheduling")
    except:
        print("An exception occured")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()

