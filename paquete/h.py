from pydub import AudioSegment
import wave
from pydub.utils import make_chunks
import os
import sox


def convert(a,b):
	os.system("sox "+a+" -r 16000 -c 1 -b 16 "+b+"p0.wav")


convert("/home/casey/Descargas/ll/aud.mp3","/home/casey/Descargas/ll/")

def ruido(a,b):
	os.system("sox "+a+" noise.wav synth whitenoise vol 0.08 && sox -m  "+a+"  noise.wav  "+b+"pr.wav")


ruido("/home/casey/Descargas/ll/p0.wav","/home/casey/Descargas/ll/")

def velocidad(a,v):
	spf = wave.open(a , "rb")
	RATE=spf.getframerate()
	signal = spf.readframes(-1)
	wf = wave.open(a, "wb")
	wf.setnchannels(1)
	wf.setsampwidth(2)
	wf.setframerate(RATE*v)
	wf.writeframes(signal)
	wf.close()

velocidad("/home/casey/Descargas/ll/pr.wav",2)



def particion(a,b,ml):
	#partir en n partes
	myaudio = AudioSegment.from_file(a, "wb") 
	chunk_length_ms = ml # pydub calculates in millisec
	chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

	#Export all of the individual chunks as wav files

	for i, chunk in enumerate(chunks):
    	 chunk_name = "chunk{0}.wav".format(i)
    		
    	 print "exporting", chunk_name

    	 chunk.export(b+chunk_name, format="wav")



particion("/home/casey/Descargas/ll/pr.wav","/home/casey/Descargas/ll/",30000)


	