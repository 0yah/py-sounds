# Import socket module
import json
import socket
import struct
import pyaudio
import wave
from record import save_wav
from play import play_sound

# Create a socket object
s = socket.socket()
p = pyaudio.PyAudio()
# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))


# receive data from the server
received_data = s.recv(1024)
received_data_header_len = struct.unpack(">H", received_data[:2])[0]
received_data_header = received_data[2:received_data_header_len+2]
received_content = received_data[received_data_header_len+2:]

print("Header: ", str(received_data_header))
print("Content: ", received_content)
header_content = json.loads(received_data_header)

# Save the received data as a WAV file
save_wav(header_content['file_name'],header_content['channels'],header_content['file_format'],header_content['rate'],received_content)

#Play the Sound received
play_sound(header_content['file_name'],header_content['chunk'])




# close the connection
s.close()
