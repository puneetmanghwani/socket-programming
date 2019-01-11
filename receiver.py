#!/usr/bin/env python2
import socket
ip="192.168.10.216"
port=8080  # port >6000 are generally free to use

#calling udp protocol

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#udp for tcp enter nothing under function and for tcp it is socket.SOCK_DGRAM and socket.AF_INET is for ipv4



#===========above this section is common for both sender/receiver==================




#binding ip and port
s.bind((ip,port))#providing a way to connect
#we have taken tuple bcs we know we always take ip and port as it is socket so taken a immutable 


print(s.recvfrom(10))



