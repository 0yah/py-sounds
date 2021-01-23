import socket
import json
import sys
import struct
import io
from play import open_sound
# class Server:
port = 12345
no_of_connections = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
s.bind(('',port))
print("Socket binded to %s" %(port))
s.listen(no_of_connections)

while True:
    clientConnection, address = s.accept()
    print("Got a connection from ",address)
       # The header has to be of fixed length
    
    sound = open_sound('output.wav')
    header = {
            'content-type': '0yah-sound',
            'content-encoding': 'utf-8',
            'content-length': "idk???",
            'byteorder': sys.byteorder,
            'channels':sound['channels'],
            'rate':sound['rate'],
            'chunk':sound['chunk'],
            'file_format':sound['file_format'],
            'file_name':sound['file_name'],
        }

    content = sound['sound']
    header_encode_data = json.dumps(header, ensure_ascii=False).encode("utf-8")
    message_hdr_len = struct.pack(">H", len(json.dumps(header, ensure_ascii=False).encode("utf-8")))

    send_data = message_hdr_len + header_encode_data + content
    clientConnection.sendall(send_data)

    clientConnection.close()






