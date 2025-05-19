# import os
# import sys
# import threading
# import socket
# 
# from pyexpat.errors import messages
# 
# 
# class Send(threading.Thread):
#     def __init__(self, sock, name):
#         super().__init__()
#         self.sock = sock
#         self.name = name
#     
#     def run(self):
#         while True:
#             print('{}: '.format(self.name), end='')
#             sys.stdout.flush()
#             message = sys.stdin.readline()[:-1]
# 
#             if message == 'QUIT':
#                 self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
#                 break
#             else:
#                 self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
# 
#         print('\nQuitting...')
#         self.sock.close()
#         os._exit(0)
#             
# class Receive(threading.Thread):
#     def __init__(self, sock, name):
#         super().__init__()
#         self.sock = sock
#         self.name = name
#         self.messages = None
#     
#     def run(self):
#         while True:
#             message = self.sock.recv(1024).decode('ascii')
#             
#             if message:
#                 if self.messages:
#                     self.messages.insert(message)
#                     print('hi')
#                 print('\r{}\n{}: '.format(message, self.name), end='')
#                 
#             else:
#                 print("No Server!")
#                 self.sock.close()
#                 os._exit(0)
#                     
# class Client:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.name = None
#         self.messages = None
#     def start(self):
#         print('Trying to connect to {}:{}...'.format(self.host, self.port))
#         self.sock.connect((self.host, self.port))
#         print('Successfully connected to {}:{}'.format(self.host, self.port))
#         
#         print()
#         self.name = input('Your name: ')
#         
#         print()
#         print('Welcome, {}! Getting ready to send and receive messages...'.format(self.name))
#         
#         send = Send(self.sock, self.name)
#         receive = Receive(self.sock, self.name)
#         
#         send.start()
#         receive.start()
#         
#         self.sock.sendall('Server: {} has joined the chat. Say hi!'.format(self.name).encode('ascii'))
#         print("\rAll set! Leave the chatroom anytime by typing 'QUIT'\n")
#         print('{}: '.format(self.name), end='')
#     
#     def send(self, text_input):
#         message = text_input.get()
#         text_input.delete(0)
#         self.messages.insert("{} : {}".format(self.name, messages))
#         
#         if message == 'QUIT':
#             self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
#             
#             print('\nQuitting...')
#             self.sock.close()
#             os._exit(0)
#         else:
#             self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
# 
# if __name__ == '__main__':
#     client = Client("127.0.0.1", 5000)
#     client.start()
#     client.messages = []
#     
#     