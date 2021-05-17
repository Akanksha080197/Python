# #Automation script template for process
# import psutil #pip install psutil (used to display process running in system)
# from sys import *

# def ProcessDisplay():
	# print("List of running processess ") #any logic which is for the automation , will ccome here 
    # Data = []
    
    
    # for proc in psutil.process_iter():
        # value = proc.as_dict(attrs = ['pid','name','username'])
        # Data.append(value)
    
    # return Data

# def main():
    # print("------Marvellous Infosystems--------- ")# banner
    # print("Script title: "+argv[0])

    # # if(len(argv)<2):
        # # print("Insufficient Arguments to the script")
        # # exit()
        
    # # if(argv[1] == "-u")or(argv[1] == "-U"): #script flag
        # # print("Use the script as Name.py Parameters")
        # # exit()
    
    # # if(argv[1] == "-h")or(argv[1] == "-H"): #script flag
        # # print("This is a demo automation script")
        # # exit()
    
    # arr=ProcessDisplay()
    # for element in arr:
    # print(element)
    
    
# if __name__ == "__main__":
    # main()
    
#https://us02st1.zoom.us/web_client/sjstu3/html/externalLinkPage.html?ref=https://psutil.readthedocs.io/en/latest/#:~:text=psutil%252520(python%252520system%252520and%252520process,the%252520management%252520of%252520running%252520processes.
    
import psutil
from sys import *

def ProcessDisplay():
    print("List of running processess")
    
    Data = []
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])#count of child process, threads count,starting time ,CPu quantum,byte allocated in ram virtual mem,no. of dynamic lib
        Data.append(value)
        
    return Data
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    arr = ProcessDisplay()
    for element in arr:
        print(element)
        
if __name__ == "__main__":
    main()    