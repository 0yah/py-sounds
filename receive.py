# Import socket module
import json
import socket
import struct
import pyaudio
import wave

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
save_file = wave.open(header_content['file_name'], 'wb') # Open the file in write only mode
save_file.setnchannels(header_content['channels'])
save_file.setsampwidth(p.get_sample_size(header_content['file_format']))
save_file.setframerate(header_content['rate'])
# Get sound from the array
save_file.writeframes(received_content)
# Close the stream
save_file.close() 



# Set chunk size of samples per data frame
chunk = header_content['chunk']
# Open the sound file
open_file = wave.open(header_content['file_name'], 'rb')  # Open stream in read only mode

# Create an interface to PortAudio
p = pyaudio.PyAudio()

 # Open a .Stream object to write the WAV file to
 # 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format=p.get_format_from_width(open_file.getsampwidth()),
                  channels=open_file.getnchannels(),
                  rate=open_file.getframerate(),
                  output=True)

  # Read data in chunks
data = open_file.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
        stream.write(data)
        data = open_file.readframes(chunk)
        if data == b'':
            break

    # Close and terminate the stream
stream.close()
p.terminate()
# close the connection
s.close()
