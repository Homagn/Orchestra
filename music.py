import getch
import pyaudio
import wave
import multiprocessing as mp

#This function is just code for playing a sound in PyAudio
def playNote(filename):

    CHUNK = 1024

    wf = wave.open(filename, 'rb')


    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == "__main__":

    while True:
        #If the 'a' key is pressed: start a new process that calls playNote
        #and pass in the file name for a note. 
        if (getch.getch() == 'A'): #a
            mp.Process(target=playNote, args=("organ.wav",)).start()

        #If the 's' key is pressed: start a new process that calls playNote
        #and pass in the file name for another note. 
        if (getch.getch() == 's'): #s

            mp.Process(target=playNote, args=("organ.wav",)).start()
