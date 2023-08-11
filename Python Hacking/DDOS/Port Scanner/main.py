import socket
import threading
from queue import Queue

target = "vi.wikipedia.org"  # The target IP address to scan for open ports.
queue = Queue()  # Queue to store the list of ports to be scanned.
open_ports = []  # List to store the open ports found during scanning.

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket using IPv4 network address.
        sock.connect((target, port))  # Attempt to connect to the target IP and port.
        return True  # If connection is successful, the port is open.
    except:
        return False  # If connection fails, the port is closed or filtered.

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)  # Add ports from the port_list to the queue.

def worker():
    while not queue.empty():
        port = queue.get()  # Get a port from the queue for scanning.
        if portscan(port):  # Check if the port is open.
            print(f"Port {port} is open!")
            open_ports.append(port)  # If open, add the port to the list of open ports.

port_list = range(1, 100000)  # Create a list of ports to be scanned (from port 1 to 1023).
fill_queue(port_list)  # Fill the queue with the list of ports.

thread_list = []

for i in range(10000):  # Create 500 worker threads to scan the ports concurrently.
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()  # Start each worker thread.

for thread in thread_list:
    thread.join()  # Wait for all worker threads to complete.

print("Open Ports Are:", open_ports)  # Print the list of open ports.

for port in open_ports:
    print(port)  # Print each open port from the list.
