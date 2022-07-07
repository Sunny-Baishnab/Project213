
#Importing All Necessary Libraries 

import socket
from threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

#Variables for First Part of the Code

SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your Computer's IP ADDRESS").strip()

#Variables for Second Part of the Code

keyboard = Controller()
screen_width = None
screen_height = None

#First Part of the Code......

def setup():
    print("\n\t\t\t\t\tWelcome to Remote Mouse\n")
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(10)
    print("\t\t\t\tSERVER is waiting for Incomming Connections...\n")
    get_devide_size()
    acceptConnections()

def acceptConnections():
    global SERVER
    while True:
        client_socket, addr = SERVER.accept()
        print(f"Connections established with {client_socket} : {addr}")

        thread1 = Thread(target = recv_message, args = (client_socket))
        thread1.start()

# Second Part of the Code.......

def get_devide_size():
    global screen_height
    global screen_width

    for m in get_monitors():
        screen_width = int(str(m).split(",")[2].strip().split("width=")[1])
        screen_height = int(str(m).split(",")[3].strip().split("height=")[1])

def recv_message(client_socket):
    global keyboard

    while True:
        try:
            message = client_socket.recv(2048).decode()
            if (message):
                keyboard.press(message)
                keyboard.release(message)
                print(message)
        
        except Exception as error:
            pass

setup()