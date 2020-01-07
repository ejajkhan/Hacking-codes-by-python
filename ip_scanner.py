import subprocess
import socket




def tcp_scan():
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    addr=""
    port=""
    result=socket_obj.connect_ex((addr,port))
    socket_obj.close()
    return result
        
