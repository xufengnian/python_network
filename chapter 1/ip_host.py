#! /usr/bin/env python
''' This python program would show your hostname and IP address
 Because my RedHat system could not transform hostname into ipaddress.so when we
 test this .py ,it will wrong.So we can annotate the 9th and 13th line to make 
 this py run. By the way,it can work on Windows opreating system'''
import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" %host_name
    print "IP address: %s" %ip_address

if __name__ == '__main__':
    print_machine_info()

