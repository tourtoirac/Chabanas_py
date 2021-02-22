import json

HEADER_LENGTH=10

def prepare_message(content):
    message_data=json.dumps(content).encode('utf-8')
    message_header=f"{len(message_data) :< {HEADER_LENGTH}}".encode('utf-8')
    message=message_header+message_data
    return message    
    
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {"header":message_header, "data":client_socket.recv(message_length)}
    except:
        return False
    
