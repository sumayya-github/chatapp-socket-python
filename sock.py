import socket
import threading
import pyfiglet
import os

os.system("tput setaf 6")
title = pyfiglet.figlet_format("\t Chat Room ... \n")
print(title)
print()
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("tput setaf 5")
sender_ip = input("Enter Your System's IP Address: ")
sender_port = int(input("Enter Your System's Port Number: "))

receiver_ip = input("Enter Your Friend's IP Address: ")
receiver_port = int(input("Enter Your Friend's Port Number: "))

skt.bind((sender_ip,sender_port))
def sender():
    while True:
        os.system("tput setaf 1")
        text = input("\nType the Message: ")
        os.system("tput setaf 2")
        skt.sendto(text.encode(),(receiver_ip,receiver_port))
        print(skt)

def receiver():
    while True:
        os.system("tput setaf 6")
        msgRcv = skt.recvfrom(1024)
        print("\nMessage from Your Friend: " + msgRcv[0].decode())

t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)
t1.start()
t2.start()

