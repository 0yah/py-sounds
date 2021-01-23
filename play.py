import pyaudio
import wave
import time
filename = 'output.wav'


def open_sound(filename):
        # Set chunk size of 1024 samples per data frame
    chunk = 1024  
    # Open the sound file 
    wf = wave.open(filename, 'rb') #Open stream in read only mode

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    file_format = p.get_format_from_width(wf.getsampwidth())
    channels = wf.getnchannels()
    rate = wf.getframerate()

    stream = p.open(format = file_format,
                    channels = channels,
                    rate = rate,
                    output = True)
    
    # Read data in chunks
    data = wf.readframes(chunk)

    while data != '':
        #print(type(data))
        data = wf.readframes(chunk)
        if data == b'':
            break
        #print((data))
    

    # Close and terminate the stream
    stream.close()
    p.terminate()
    return {
        "sound":data,
        "rate":rate,
        "file_format":file_format,
        "chunk":chunk,
        "channels":channels,
        "file_name":f'{round(time.time() * 1000)}.wav'
    }



def play_sound(filename):
    # Set chunk size of 1024 samples per data frame
    chunk = 1024  
    # Open the sound file 
    wf = wave.open(filename, 'rb') #Open stream in read only mode

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    # Read data in chunks
    data = wf.readframes(chunk)    

    # Play the sound by writing the audio data to the stream


    while data != '':
        #print(type(data))
        stream.write(data)
        data = wf.readframes(chunk)
        if data == b'':
            break
        #print((data))
    

    # Close and terminate the stream
    stream.close()
    p.terminate()

def play_bytes(sound,channel,rate,file_format,chunk):
    # Set chunk size of 1024 samples per data frame
    # Open the sound file 
    wf = wave.open('filename', 'rb') #Open stream in read only mode

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = file_format,
                    channels = channel,
                    rate = rate,
                    output = True)

    # Read data in chunks
    data = wf.readframes(chunk)
    

    # Play the sound by writing the audio data to the stream

    while data != '':
        #print(type(data))
        stream.write(data)
        #data = wf.readframes(chunk)
        if data == b'':
            break
        #print((data))

    # Close and terminate the stream
    stream.close()
    p.terminate()


#play_sound(filename)