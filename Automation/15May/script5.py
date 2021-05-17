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
																  
    if(len(output)>0):
        print("There are duplicate files")
    else:
        print("There are no duplicate files")
        return
 
    print("List of duplicate files are")
    i = 0
    icnt = 0 #var creation 
    for result in output: #1st iteration ->(a.txt,b.txt,c.txt) , #2nd iteration ->hello.txt,demo.txt,c.txt)
        icnt = 0 #var re initialisation
        for path in result: # a.txt then b.txt then c.txt 
            icnt +=1
            if icnt >= 2:
                i+=1
            print("Duplicate files are ")
            print(path)
            print("Do you want to delete these duplicate files? Y/N")
            response=(input())
            if response == 'Y':
                os.remove(path)
            else:
                exit()
    
        
            
def main():
    print("Marvellous Infosystems")
    print("Directory traversal script")
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or  (argv[1] == "-H"):
        print("It is a Directory cleaner script")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Provide the absolute path of the target director")
        exit()
        
    if os.path.exists(argv[1]) == True:
        print("Input path exists")
    else:
        print("Path does not exists")
        exit()
        
    if os.path.abspath(argv[1]) == argv[1]:
        print("Path is absolute")
    else:
        print("Path is not absolute")
        argv[1] = os.path.abspath(argv[1])
        print(argv[1])

    arr = {}
    
    arr = DirectoryTraversal(argv[1])
    DisplayDuplicate(arr)

if __name__ == "__main__":
    main()

