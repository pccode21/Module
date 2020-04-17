from scapy.all import srp, Ether, ARP
IpScan = '10.117.53.1/24'
try:
    ans, unans = srp(Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(pdst=IpScan), timeout=2)
    # srp 在第2层发送和接收数据包
except Exception as e:
    print(e)
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf('%Ether.src%...%ARP.psrc%')
        print(ListMACAddr)
