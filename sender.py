#!/usr/bin/env python2
import socket
ip="192.168.10.216"
port=8080  # port >6000 are generally free to use

#calling udp protocol

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#udp for tcp enter nothing under function and for tcp it is socket.SOCK_DGRAM and socket.AF_INET is for ipv4



#sending message to target


s.sendto("hiiii",(ip,port))
