#walk function in OS -> allow the traversal in the directory even in nested form  , self recursive
#Three return values :->1. names of files
#2.names of subdirectories 
#3.parent folder 
#absolute path should be given , or else where the directory is present there the .py file should be there 



from sys import*
import os

def DirectoryTraversal(path):
    print("Contents of the directory are ")
    
    for folder,subfolder,filename in os.walk(path): #folder -> Demo , Subfolder ->Hello, filename ->a.py , b.py , all these 3 para are list 
        print("Directory name is:"+folder)
        for sub in subfolder:
            print("Subfolder of "+folder+"is"+sub)
        for file in filename:
            print("file name is:"+file)
            
def main():
	print("Marvellous Infosystems")
	print("Directory traversal script")
	
	if(len(argv)!=2):
		print("Error : Invalid number of arguments")
		exit()
		
	if(argv[1] == "h")or(argv[1]=="H"):
		print("It is a directory cleaner script")
		exit()
		
	if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Provide the absolute path of the target director")
        exit()

    DirectoryTraversal(argv[1])
		
if __name__ == "__main__":
	main()