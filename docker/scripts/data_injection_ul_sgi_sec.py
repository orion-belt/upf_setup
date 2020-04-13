from scapy.all import *
from scapy.contrib.gtp import GTP_U_Header

data= "Orange Lab Network - SGI Seconary"

sendp(Ether(dst="00:0c:29:46:1f:53")/
	IP(src="172.20.16.3",dst="172.20.16.2")/
	UDP(dport=2152)/GTP_U_Header(teid=5678)/
	IP(src="20.20.20.20",dst="172.23.16.3",version=4)/
	UDP()/data, iface="n3")
