import pyfiglet
import socket
import time
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
ascii_banner = pyfiglet.figlet_format("RIZARSCANN")
print(ascii_banner)
print('Port scanning tool made by CBDEVSEC 2024 // please use responsibly //')
print("------------------------------")
target = input('What you want to scan?: ')
 

target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)
 
begin = int(input("start port: "))
end = int(input("end port: "))

 
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
 
 
start = time.time()
 

for port in range(begin, end):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')
 
end = time.time()
print(f'Time taken {end-start:.2f} seconds')