#!/usr/bin/python2.7

import socket as sk
import subprocess
target_ip = raw_input("Enter target IP and press enter: ")
subprocess.call(["clear"])
for port in range(1, 65535):
  try:
	s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
	s.settimeout(1000)
	s.connect((target_ip,port))
	print '%d:OPEN' % (port)
	s.close
  except: continue
