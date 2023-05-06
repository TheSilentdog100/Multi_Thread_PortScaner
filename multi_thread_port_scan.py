import socket
import threading
import time

start = time.perf_counter()

THREAD_COUNT = int(input("Enter your desired thread Count\nrecommended (30-250) depending on your system\n"))
IP_ADRESS = input("Enter target Ip adress\n")
AVAILABLE_PORTS = []

with open("open_ports.txt","a") as file:
    file.write(IP_ADRESS+"\n")


for i in range(65536): #create List with all available Ports:
    AVAILABLE_PORTS.append(i)

threads = []

def checkPorts():
    while AVAILABLE_PORTS:
        port = AVAILABLE_PORTS.pop(0)
        progress = 65536-len(AVAILABLE_PORTS)
        progress = (progress/65536)*100
        progress = round(progress,1)
        print(f'Progress: {progress} %' ,end="\r")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            try:
                s.connect((IP_ADRESS, port))
                print(f"{port} is open                         ")
                with open("open_ports.txt", "a") as file:
                    file.write(f"port {port} is open\n")
            except:
                pass


for i in range(THREAD_COUNT):
    t = threading.Thread(target=checkPorts)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"Finished: 100% in {round(finish-start,2)} seconds             ")
