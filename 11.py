#!/usr/bin/python3
#pingscanner.py
import sys


print(".88b  d88. .d8888.    .d8b.  d8888b. db    db d88888b d8b   db d888888b db    db d8888b. d88888b d88888b ")
print(" 88'YbdP`88 88'  YP   d8' `8b 88  `8D 88    88 88'     888o  88 `~~88~~' 88    88 88  `8D 88'     88' ")   
print(" 88  88  88 `8bo.     88ooo88 88   88 Y8    8P 88ooooo 88V8o 88    88    88    88 88oobY' 88ooooo 88ooooo ")
print(" 88  88  88   `Y8b.   88~~~88 88   88 `8b  d8' 88~~~~~ 88 V8o88    88    88    88 88`8b   88~~~~~ 88~~~~~ ")
print(" 88  88  88 db   8D   88   88 88  .8D  `8bd8'  88.     88  V888    88    88b  d88 88 `88. 88.     88. ")    
print(" YP  YP  YP `8888Y'   YP   YP Y8888D'    YP    Y88888P VP   V8P    YP    ~Y8888P' 88   YD Y88888P Y88888P ")


from scapy.all import *
print("pinging the target....")
ip = sys.argv[1]    # command line argument
icmp = IP(dst=ip)/ICMP()
#IP defines the protocol for IP addresses
#dst is the destination IP address
#TCP defines the protocol for the ports
resp = sr1(icmp,timeout=10)
if resp == None:
    print("This host is down")
else:
    print("This host is up")