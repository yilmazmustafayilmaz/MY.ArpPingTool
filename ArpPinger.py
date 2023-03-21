import argparse
import scapy.all as scapy

class ArpPing():

    def __init__(self):
        print("Arp Ping Başlatıldı..")

    def get_user_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ipaddress', type=str, help="ip adresini girmelisiniz")
        args = parser.parse_args()

        if args.ipaddress != None:
            return args
        else:
            print("ip adresini -i argümanı ile giriniz")

    def arp_request(self, ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combine_packet = broadcast_packet/arp_request_packet
        (answerwd_list, unanswared_list) = scapy.srp(combine_packet, timeout=1)
        answerwd_list.summary()

if __name__ == "__main__":
    arp_ping = ArpPing()
    get_user_input = arp_ping.get_user_input()
    arp_ping.arp_request(get_user_input.ipaddress)
