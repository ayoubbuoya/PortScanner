#importing
import socket
from datetime import datetime
import os
import subprocess
#Clear secreen
subprocess.call('clear',shell=True)
#data inputs
Server_host=socket.gethostname()
Server_Ip=socket.gethostbyname(Server_host)
#beuatifull banner 
print("-"*84)
print("")
print("      Scanning Remote Ip : "+Server_Ip)
print("")
print("-"*84)
#check what time the scan started
t1=datetime.now()
#Scan Ports with printing the Error
try :
    for port in range(1,1025) :
        sock=socket.socket()
        result=sock.connect_ex((Server_Ip,port))
        #this fuction will return 0 if the port is open
        if result== 0 :
            print("port{} =====> Is Open ".format(port))
        else :
            print("port{} =====> Is Closed ".format(port))
        sock.close()
except KeyboardInterrupt :
        print("Exiting ..............")
        sys.exit()
except socket.gaierror :
        print("Socket Name Can not resolved ")
        print("")
        print("Exiting ..............") 
        sys.exit()
except socket.error :
        print("Can't Connet To Server ")
        sys.exit()
#Check time again
t2=datetime.now()
#total time of running this script
time=t2-t1
print("")
print(" [ "+" AyoubBuoya "*3+" ]  ")
print("")
print("    Script Run For ===> {} S".format(time))
print("")
print("")
print(" [ "+" AyoubBuoya "*3+" ]  ")

        
        
        
