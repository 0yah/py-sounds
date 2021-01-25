import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3  # How long the clip should be
filename = "output.wav"




def record_wav(sample_format,channels,fs,chunk,seconds):

    p = pyaudio.PyAudio()
    print("Recording...")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []  # Initialze array to store frames

    for i in range(0, int(fs/chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio Interface
    p.terminate()
    print("Finished recording...")
    return frames




def save_wav(filename,channels,sample_format,fs,frames):
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb') # Open the file in write only mode
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    # Get sound from the array
    wf.writeframes(b''.join(frames))

    # Close the stream
    wf.close() 


if __name__ == '__main__':
    frames = record_wav(sample_format,channels,fs,chunk,seconds)
    save_wav(filename,channels,sample_format,fs,frames)
