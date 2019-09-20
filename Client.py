import socket
import pickle
import datetime
import time
import random


class TCPClientHandler:
    
    def __init__(self, socket):
        self.clientS = socket
       
        
    def getUser(self):
        data = {"Option": 1}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
        print("Client has sent the data")
        

    def sendMessage(self):
        print("this is inside sendMessage")
        

    def getMessages(self):
        print("this is inside getMessages")
        
    
    def createChannel(self):
        print("this is inside createCHannel")
        
    
    
    def getChoice(self):
        print("\n\n")
        print("******* TCP Message App ******** \n--------------------------------\n"+
              "Options Available:")
        print("1. Get user list\n"+
              "2. Send a message\n"+
              "3. Get my messages\n"+
              "4. Create a new channel\n"+
              "5. Chat in a channel with your friends\n"+
              "6. Disconnect from server")
        
        choice = int(input("Input: "))
        switcher = {
            1: self.getUser,
            2: self.sendMessage,
            3: self.getMessages,
            4: self.createChannel
        }
        func = switcher.get(choice, lambda: print("Choice must be from 1-4"))
        func()
        #return func()
        

def init_prompt():

    HOST = str(input("Enter the server IP Address: "))
    PORT = int(input("Enter the server port: "))
    ID = input("Your id key (i.e your name): ")
    return [HOST, PORT, ID]


def menuChoice(choice):
    pass


def connect(HOST, PORT, ID):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        
       
        ################################   SENDING DATA   ###########################
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 2}
        data_serialized = pickle.dumps(data)
        client.send(data_serialized)
        print("Client has sent the Data")
        
        
        
        ###############################  Recieving Data   ############################
        server_response = client.recv(1024)
        server_data = pickle.loads(server_response)
        
        client_id = server_data['client_id']
        server_msg = server_data['msg_from_server']

        #print data and close client

        print("Client " + str(client_id) + " successfully connected to server")
        print("Server says: " + server_msg)
        TCHP = TCPClientHandler(client)
        
        
        
        while True:
            
            
            #TCHP.getChoice()
            
            ########################### Recieving data #####################
            # server_response = client.recv(1024)
            # data = pickle.loads(server_response)
            # print("recieved")
            # print(f"Recieved data is: {data}")
            
            
            ###############################  Sending Data   ############################ 
            TCHP.getChoice()
            time.sleep(3)
            # time.sleep(3)
            # data = {"client_name": random.randint(1,10), "sent_on": datetime.datetime.now(), "Option": 2}
            # data_serialized = pickle.dumps(data)
            # client.send(data_serialized)
            # print("Sending Data")
            
        
       
    except socket.error as socket_exception:
        print(socket_exception)  
    print("Closing client")
    client.close()
  





#result = prompt()
PORT = 6969
HOST = socket.gethostbyname(socket.gethostname())
ID = 'aang'

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969
print("Host is: " + HOST)
print("Port is: " + str(PORT))

#connect(HOST, PORT, ID)

test = TCPClientHandler(None)
func = test.getChoice()
##################################################################################
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))
# HEADERSIZE = 10

# while True:
    
#     full_msg = b''
#     new_msg = True
#     while True:
#             msg = client.recv(1024)
#             if new_msg:
#                     print(f"new message length: {msg[:HEADERSIZE]}")
#                     msglen = int(msg[:HEADERSIZE])
#                     new_msg = False
#             full_msg += msg
            
#             if len(full_msg) - HEADERSIZE == msglen:
#                 print("full msg recvd")
#                 d = pickle.loads(full_msg[HEADERSIZE:])
#                 print()

#                 new_msg = True
#                 full_msg = b''





#TCPH.getChoice(1)






