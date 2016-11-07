#! /usr/bin/env python
'''This python programming will transform remote website'url into ipaddress'''

import socket
import argparse

def get_remote_machine_info(remote_host):
    #remote_host = 'www.baidu.com' #we can change it as any url
    try:
        print "IP address: %s" %socket.gethostbyname(remote_host)
    except socket.error,err_msg:
        print "%s: %s" %(remote_host,err_msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' input remote url ')
    parser.add_argument('-r ',action="store",dest="remote_host",required=True)
    give_args = parser.parse_args()
    remote_host = give_args.remote_host
    get_remote_machine_info(remote_host)
    
