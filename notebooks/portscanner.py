# for educational purposes only
import socket
import sys
from datetime import datetime
import subprocess 
ip_array=[]
for ping in range(1,10): 
    address = "127.0.0." + str(ping) 
    res = subprocess.call(['ping', '-c', '3', address]) 
    if res == 0: 
        ip_array.append(address)


#ip = input("Enter the Ip of the Server you want to scan: ")

t1 = datetime.now()

for i in ip_array:
    try:
        try:
    
            for port in range(1,65535):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip_array[i], port))
            if result == 0:
                print ("port{}:     open".format(port))
                sock.close
        except KeyboardInterrupt:
            sys.exit

        except socket.error:
            print("invalid IP")
            sys.exit
    except socket.error:
        sys.exit
        
t2 = datetime.now()
time = t2 - t1
print(time) 
