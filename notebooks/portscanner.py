import socket
import sys
from datetime import datetime

ip = input("Enter the Ip of the Server you want to scan: ")


t1 = datetime.now()
try:

    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print ("port{}:     open".format(port))
        sock.close
except KeyboardInterrupt:
    sys.exit

except socket.error:
    print("invalid IP")
    sys.exit
t2 = datetime.now()
time = t2 - t1
time = str(time)
print("It took " + time)
