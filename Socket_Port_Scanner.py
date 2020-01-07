#the idea of a port scanner is to run through a ist of ports
#testing to see if they are open
#we can do this steps for using sockets for sending data 
# #first you make the connection,then try to offload the request
#this is a form of "reconnainssance" for hackers and penetration testers


from socket import *
x=0
ip=input("Enter ip to scan: ")
start=int(input("Enter starting port number: "))
end=int(input("Enter ending port number: "))
print("Scanning The given ip: ",ip)
print("\n\n")
for port in range(start,end):
    print(" port :  ",port)
    s=socket(AF_INET,SOCK_STREAM)
    s.settimeout(2)
    if s.connect_ex((ip,port))==0:
        print("port: ",port," is open")
        x=x+1
    s.close()
print("Scanning is compete..\n",x," ports are open")
      

