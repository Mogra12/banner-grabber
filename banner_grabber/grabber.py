import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("IP: ")
    port = str(input("Port: "))
    banner(ip, port)
    
main()