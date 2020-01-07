import socket
import ip_scanner as scanner
hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
print("Computer name :  ",hostname)
print("IP Address :  ")
result=scanner.tcp_scan()
for i in result:
    print(i)
