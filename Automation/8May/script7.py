import os
import time
import psutil
from sys import *
import schedule

i = 0
def ProcessDisplay(FolderName = "Marvellous"):
    
    global i
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    File_Path = os.path.join(FolderName,"Marvellous%s.log"%i)
    i = i+1
    #File_path = (File_path.replace(" ","").replace(":",""))
    fd = open(File_Path,"w")
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n"% element)
		
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Scheule_Time Directory_Name")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processess")
        exit()
     
    try:
        schedule.every(int(argv[1])).minutes.do(ProcessDisplay)
    except:
        print("An exception occured")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()