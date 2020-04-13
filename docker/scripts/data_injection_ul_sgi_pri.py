from scapy.all import *
from scapy.contrib.gtp import GTP_U_Header

data= "Orange Lab Network - SGI Primary"

sendp(Ether(dst="00:0c:29:46:1f:53")/
	IP(src="172.20.16.3",dst="172.20.16.2")/
	UDP(dport=2152)/GTP_U_Header(teid=1234)/
	IP(src="10.10.10.10",dst="172.22.16.3",version=4)/
	UDP()/data, iface="n3")
