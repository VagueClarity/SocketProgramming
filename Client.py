import socket
import pickle
import datetime
import time
import random


class TCPClientHandler:
    
 
    
    def __init__(self, socket):
        self.clientS = socket
       
        
    def getUser(self):
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 1}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
        print("Client has sent the data")
        

    def sendMessage(self):
        
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 2}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
        
        

    def getMessages(self):
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 3}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
        
    
    def createChannel(self):
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 4}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
        
        
    def chatting(self):
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 5}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
    
    def disconnect(self):
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 6}
        s_data = pickle.dumps(data)
        self.clientS.send(s_data)
    
    
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
            4: self.createChannel,
            5: self.chatting,
            6: self.disconnect
            
        }
        func = switcher.get(choice, lambda: print("Choice must be from 1-6"))
        func()
        #return func()
        

def init_prompt():

    HOST = str(input("Enter the server IP Address: "))
    PORT = int(input("Enter the server port: "))
    ID = input("Your id key (i.e your name): ")
    return [HOST, PORT, ID]



class Client:
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    
    def __init__(self, host = socket.gethostbyname(socket.gethostname()) , port = 6969, ID = 'Aang'):
        self.host = host
        self.port = port
        self.ID = ID
        
        
    def run(self):
        self.client.connect((self.host, self.port))
        self.connected = True
        
        
    def sendData(self, data): 
        #data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 2}
        data_serialized = pickle.dumps(data)
        self.client.send(data_serialized)
        print("Client has sent the Data")
    
    def recieveData(self):
        server_response = self.client.recv(1024)
        if len(server_response) > 0:
            server_data = pickle.loads(server_response)
            return server_data
        else:   
            return None
    
    def getClientSocket(self):
        return self.client
    
    def stop(self):
        self.connected = False
        self.client.close()
        
    def isConnected(self):
        return self.connected
    
    def setConnected(self, flag = True):
        self.connected = flag
        
        
    
    
def connect(HOST, PORT, ID):
    try:
       
        
        c = Client(HOST, PORT)
        c.run()
        client = c.getClientSocket()
        
        data = {"client_name": ID, "sent_on": datetime.datetime.now(), "Option": 2}
        ############################## Sending Dat ################################
        c.sendData(data)
    
  
        ###############################  Recieving Data   ############################

        server_data = c.recieveData()
        
        client_id = server_data['client_id']
        server_msg = server_data['msg_from_server']
        print("Client " + str(client_id) + " successfully connected to server")
        print("Server says: " + server_msg)
        TCHP = TCPClientHandler(client)
        
        while True:
            
            ############################## Sending Data #############################
            TCHP.getChoice()
            
            ########################### Recieving data #####################
            clients = c.recieveData()
            print("recieved")
            print(f"Recieved data is: {clients}")
            # if !clients["flag"]:
            #     c.setConnected()
            time.sleep(2)
           
        
       
    except socket.error as socket_exception:
        print(socket_exception)  
    print("Closing client")
    c.stop()
  





#result = prompt()
PORT = 6969
HOST = socket.gethostbyname(socket.gethostname())
ID = 'aang'

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969
print("Host is: " + HOST)
print("Port is: " + str(PORT))

connect(HOST, PORT, ID)

#test = TCPClientHandler(None)
#test.getChoice()
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






