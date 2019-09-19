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
        
        client_id = address[1]
        clients.append(client_id)
        
        while True:
            request_from_client = clientsocket.recv(1024)
            
            if(request_from_client):
                data = pickle.loads(request_from_client)
              
                
                client_name = data['client_name']
                date = data['sent_on']
                print(f"Client {client_name} with clientid: {client_id} has connected to this server")
            
                server_msg = "Hello from server"    
                server_response = {"client_id": client_id, "msg_from_server": server_msg}
                serialized_data = pickle.dumps(server_response)
                #serialized_data = bytes(f'{len(serialized_data):< {HEADERSIZE}}', "utf-8") + serialized_data
                clientsocket.send(serialized_data)  
            
        print("Closing clientSocket")
        clientsocket.close()
       
    # client Id assigned by server to client
    except socket.error as socket_error:
        print(socket_error)
        pass
    print("closing server")
    server.close()
  


    
    

