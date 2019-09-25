import socket
import pickle
import datetime
import sys


HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969
HEADERSIZE = 10
MAX_NUM_CONNECTION = 5
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(MAX_NUM_CONNECTION)
print(f"Server Info \nIP Address: {HOST}\nport listening: {PORT}")
print("Waiting for connection...")

clients = []






while True:

    try:
        clientsocket, address = server.accept()
        
        
        ########## First Connection ############################
        client_id = address[1]
        clients.append(client_id)
        
        
        ###############################  Recieving Data   ############################ 
        request_from_client = clientsocket.recv(1024)
        data = pickle.loads(request_from_client)
        client_name = data['client_name']
        date = data['sent_on']
        print(f"Client {client_name} with clientid: {client_id} has connected to this server")
        
        while True:
           
            ##############################  Sending Data   ############################
            server_msg = "Hello from server"    
            server_response = {"client_id": client_id, "msg_from_server": server_msg}
            serialized_data = pickle.dumps(server_response)
            #serialized_data = bytes(f'{len(serialized_data):< {HEADERSIZE}}', "utf-8") + serialized_data
            
            clientsocket.send(serialized_data)  
            
            
            ###############################  Recieving Data   ############################   
            option = clientsocket.recv(1024)
            pickledOption = pickle.loads(option)
            print(f"recieved choice: {pickledOption['Option']}" )
            if pickledOption["Option"] == 1:
                
                ########################### Send Data #####################################
                s_clients = pickle.dumps(clients)
                clientsocket.send(s_clients)
                print(f'sending data back: {clients[0]}')
            
            if pickledOption["Option"] == 6:
                data = {"flag": False, "msg": "You have been disconnected from server."}
                s_clients = pickle.dumps(data)
                clientsocket.send(s_clients)
                clientsocket.close()
                
            
        print("Closing clientSocket")
        clientsocket.close()
       
    # client Id assigned by server to client
    except (socket.error, EOFError):
        #print("An exception as occured")
        pass
    
    
    server.close()
    print("closing server")
  


    
    

