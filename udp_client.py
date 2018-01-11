from socket import *
from struct import *


def main():
    #sock = socket(AF_INET, SOCK_DGRAM)
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_UDP)
    data = 'Raw World!'

    udp_src_port = 10010
    udp_dest_port = 10000
    length = 8 + len(data)
    checksum = 0

    udp_header = pack('!4H', udp_src_port, udp_dest_port, length, checksum)
    packet = udp_header + data.encode()

    sock.sendto(packet, ('192.168.1.110', 10000))

    '''
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_id = htons(54321)
    ip_frag_off = 0
    ip_proto = IPPROTO_UDP
    ip_ttl = 255
    ip_check = 0
    ip_tlen = (4 * ip_ihl) + len(data)

    ip_src_addr = inet_aton('192.168.1.110')
    ip_dest_addr = inet_aton('192.168.1.110')

    ip_header = pack('!2B3H2BH4s4s', (ip_ver << 4) + ip_ihl, ip_tos,
                     ip_tlen, ip_id, ip_frag_off, ip_ttl,
                     ip_proto, ip_check, ip_src_addr, ip_dest_addr)

    packet = (ip_header + udp_header + data.encode())
    sock.connect(('192.168.1.110', 10010))
    #sock.sendto(packet, ('192.168.1.110', 10000))
    sock.send(packet)
    '''

if __name__ == '__main__':
    main()
