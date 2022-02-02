from scapy.all import *
import sys
 
try:
    interface = input("[*] Enter Desired Interface: ")
except KeyboardInterrupt:
    print("[*] User Requested Shutdown...")
    print("[*] Exiting...")
    sys.exit(1)
 
def querysniff(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst    
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            print(ip_src)
            print(ip_dst)
            print(pkt.getlayer(DNS).qd.qname)
 
sniff(iface = interface,filter = "port 53", prn = querysniff, store = 0)
print("\n[*] Shutting Down...")