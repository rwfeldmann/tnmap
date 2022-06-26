#!/usr/bin/python
import subprocess
import sys
import time
import netaddr

SUBNET_PREFIXLEN = 24
ip = netaddr.IPNetwork(sys.argv[1])

if SUBNET_PREFIXLEN < ip.prefixlen:
	subnet_list = [ip,]
else:
	subnet_list = ip.subnet(SUBNET_PREFIXLEN)

for sub in subnet_list:
	cmd = [
           #'nmap',
	       #'-T4',	#use aggressive timings
	       #'--open',	#only return open ports
	       #'-sT',	#SYN scan
	       #'-n',	#dont' attempt DNS resolution
	       #'-vvv',	#super verbose
	       #'--min-rate=1000',	#set min packet transmission rate
	       #'--min-hostgroup=256'	#how many hosts to scan at the same time
	       #'--max-retries=2',	#how many retries per host
	       #'-sC',	#run script defaults
	       #'-PN', # treat all hosts as online, don't ping
	       #'-oX', 'out/%s_%s' % (sub.ip,sub.prefixlen), #XML output to stdout
	       str(sub)	#target specification
	      ]
	print(' '.join(cmd))
