#Automation script template 
from sys import *

def Function(value):
	print("Inside function with parameter:" +value) #any logic which is for the automation , will ccome here 


def main():
    print("------Marvellous Infosystems--------- ")# banner
    print("Script title: "+argv[0])

    if(len(argv)<2):
        print("Insufficient Arguments to the script")
        exit()
        
    if(argv[1] == "-u")or(argv[1] == "-U"): #script flag
        print("Use the script as Name.py Parameters")
        exit()
    
    if(argv[1] == "-h")or(argv[1] == "-H"): #script flag
        print("This is a demo automation script")
        exit()
    
    Function(argv[1])
    
    
if __name__ == "__main__":
    main()