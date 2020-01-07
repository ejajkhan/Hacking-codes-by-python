import socket

def funbanner(ip,port):
    try:
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return






def main():
    ip1='136.243.69.14'
    port=21
    banner1=funbanner(ip1,port)
    if banner1:
        print("ip:  ",ip1,"banner1:     ",banner1)
