import logging
from scapy.all import sniff, IP, TCP, UDP, ICMP

# Configure logging
logging.basicConfig(filename='packet_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if proto == 6:  # TCP
            protocol = "TCP"
        elif proto == 17:  # UDP
            protocol = "UDP"
        elif proto == 1:  # ICMP
            protocol = "ICMP"
        else:
            protocol = "Other"

        packet_info = f"Source: {ip_src}, Destination: {ip_dst}, Protocol: {protocol}"
        print(packet_info)
        logging.info(packet_info)

        if protocol in ["TCP", "UDP"]:
            payload = bytes(packet[protocol].payload)
            print(f"Payload: {payload.decode('utf-8', errors='replace')}\n")
            logging.info(f"Payload: {payload.decode('utf-8', errors='replace')}")
        elif protocol == "ICMP":
            print(f"ICMP Type: {packet[ICMP].type}, Code: {packet[ICMP].code}\n")
            logging.info(f"ICMP Type: {packet[ICMP].type}, Code: {packet[ICMP].code}")

def start_sniffing(packet_count, timeout):
    print("Starting packet capture...")
    try:
        sniff(prn=packet_callback, store=0, count=packet_count, timeout=timeout)
    except Exception as e:
        print(f"Error: {e}")

while True:
    user_input = input("Press Enter to start packet capture, or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    elif user_input.strip() == "":
        packet_count = int(input("Enter the number of packets to capture: "))
        timeout = int(input("Enter the capture timeout (in seconds): "))
        start_sniffing(packet_count, timeout)
    else:
        print("Invalid input. Please try again.")
