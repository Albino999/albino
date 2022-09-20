
#TESTING
import socket
import os
from time import sleep
from turtle import ht
os.system('cls')
def ping():
    server1= input("Input Host >>")
    addr= socket.gethostbyname(server1)
    print("SUCSESS >> {}".format(addr))
def host_name():
    host_name = socket.gethostname()
    print ('Hostname: '+(ht))
def ip_address():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    print ('Your IP Address: '+(ip))

def main_menu():
    print ('Main Menu:')
    print ('1. PINGGER')
    print ('2. Cek MY Hostname')
    print ('3. Check My IP Address')
main_menu()

opsi = input('Choose >>')
if opsi == '1':
    ping()
elif opsi == '2':
    host_name()
elif opsi == '3':
    ip_address()
else:
    print ('Wrong Key! Wait...')
    sleep(3)
    os.system('cls')
    main_menu()
i = 
