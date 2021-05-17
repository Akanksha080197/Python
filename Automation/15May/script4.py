from sys import *
import os
import hashlib

def CalculateChecksum(path, blocksize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()
    
    buffer = fd.read(blocksize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()
def DirectoryTraversal(path):
    print("Contents of the directory are")
    
    duplicate = {} #dictionary to hold checksum and file name 
    
    for Folder , Subfolder , Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:
            print("Subfolder of  " + Folder + "is "+ sub)
        for file in Filename:
            print("File name is : "+file)
            actualpath = os.path.join(Folder,file)
            hash = CalculateChecksum(actualpath)
            
            if hash in duplicate: #that checksum is already present
                duplicate[hash].append(actualpath)
            else:
                duplicate[hash]=[actualpath]
                
    return duplicate
    
def DisplayDuplicate(duplicate):
    output = list(filter(lambda x : len(x)>1,duplicate.values())) #duplicate.values() -> gives the file path  , value of all the keys  i.e list 
                                                                  #list considered as x , if len of x is greater than 1 then  only new list will be created else not
#duplicaate = ((a.txt,b.txt,c.txt) ,(data.txt),(hello.txt,demo.txt,c.txt),(marvellous.txt))                                                                  
#output = ((a.txt,b.txt,c.txt),(hello.txt,demo.txt,c.txt)) len = 2 , not 6

    
    if(len(output)>0):
        print("There are duplicate files")
    else:
        print("There are no duplicate files")
        return
 
    print("List of duplicate files are")
    icnt = 0 #var creation 
    for result in output: #1st iteration ->(a.txt,b.txt,c.txt) , #2nd iteration ->hello.txt,demo.txt,c.txt)
        print(result)
        icnt = 0 #var re initialisation
        for path in result: # a.txt then b.txt then c.txt 
            icnt +=1
            if icnt >= 2:
                print("%s"%path)
                os.remove(path)
                print("removed")
        
            
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

    arr = {}
    
    arr = DirectoryTraversal(argv[1])
    DisplayDuplicate(arr)
if __name__ == "__main__":
    main()

