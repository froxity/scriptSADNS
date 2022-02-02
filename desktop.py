import os
import pihole
from scapy import *
from scapy.all import sniff
from scapy.all import ARP
from scapy.all import DNSQR
from scapy.all import UDP
from scapy.all import IP
from scapy.all import IPv6
from scapy.all import DNS
# from subprocess import Popen

# os.system('python pihole.py -d db1.sqlite')
# p = subprocess.Popen(['python', 'pihole.py'])
import subprocess as sp

extProc = sp.Popen(['python','pihole.py']) # runs myPyScript.py 
status = sp.Popen.poll(extProc)