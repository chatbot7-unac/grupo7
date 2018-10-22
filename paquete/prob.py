from pydub import AudioSegment
from pydub.playback import play
import wave
from pydub.utils import make_chunks
import os
import sox


UPLOAD_FOLDER="/home/casey/Escritorio/bd/"
#dest="/home/casey/Escritorio/aglomerado"



def convert(dest):
	for archivo in os.listdir(UPLOAD_FOLDER):        #  listdir ,devuelve una lista que contiene los nombres de las entradas en el directorio dado por ruta.
				
				name_f=archivo
				name_file=archivo.split('.')
				#gg=".".join(name_file)

				print(archivo)
				if(name_file[1]=='mp3'):	
					os.system("sox "+UPLOAD_FOLDER+"/"+name_f+" -r 16000 -c 1 -b 16 "+dest+"/"+name_file[0]+"_t.wav")

	
#convert("/home/casey/Escritorio/bd/")




def ruido(dest):
	
	for archivo in os.listdir(UPLOAD_FOLDER):
				if archivo.endswith("_t.wav"):

					name_file=archivo.split('.')
					
					print(archivo)
			
					if(name_file[1]=='wav'):		
						os.system("sox " +UPLOAD_FOLDER+"/"+archivo+"  noise.wav  synth whitenoise vol 0.08 && sox -m  "+UPLOAD_FOLDER+"/"+archivo+"   noise.wav   "+dest+"/"+name_file[0]+"_r.wav")


#ruido("/home/casey/Escritorio/bd/")



def velocidad(dest,v):
	for archivo in os.listdir(UPLOAD_FOLDER):
				if archivo.endswith("_r.wav"):

					name_file=archivo.split('.')
					
					print(archivo)
			
					if(name_file[1]=='wav'):

						spf = wave.open(dest+"/"+archivo , "rb")
						RATE=spf.getframerate()
						signal = spf.readframes(-1)	
						wf = wave.open(dest+"/"+archivo , "wb")
						wf.setnchannels(1)
						wf.setsampwidth(2)
						wf.setframerate(RATE*v)
						wf.writeframes(signal)
						wf.close()

#velocidad("/home/casey/Escritorio/bd/",2)




def particion(dest,ml):
	for archivo in os.listdir(UPLOAD_FOLDER):
				if archivo.endswith("_r.wav"):

					name_file=archivo.split('.')
					
					print(archivo)
			
					if(name_file[1]=='wav'):



						#partir en n partes
						myaudio = AudioSegment.from_file(UPLOAD_FOLDER+"/"+archivo, "wb") 
						chunk_length_ms = ml # pydub calculates in millisec
						chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

						#Export all of the individual chunks as wav files

						for i, chunk in enumerate(chunks):
    	 					 chunk_name = "parte{0}.wav".format(i)
    		
    	 					 print "exporting", chunk_name

    	 					 chunk.export(dest+chunk_name, format="wav")



#particion("/home/casey/Escritorio/bd/",30000)



#dest="/home/casey/Escritorio/audio"
#myAudioFile="aud.mp3"
def extraccion_fondo(dest):
	for archivo in os.listdir(UPLOAD_FOLDER):
				if archivo.endswith(".mp3"):

					name_file=archivo.split('.')
					
					print(archivo)
			
					if(name_file[1]=='mp3'):

						# read in audio file and get the two mono tracks
						sound_stereo = AudioSegment.from_file(dest+"/"+archivo ,format="mp3")
						sound_monoL = sound_stereo.split_to_mono()[0]
						sound_monoR = sound_stereo.split_to_mono()[1]

						# Invert phase of the Right audio file
						sound_monoR_inv = sound_monoR.invert_phase()

						# Merge two L and R_inv files, this cancels out the centers
						sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

						# Export merged audio file
						file_name=myAudioFile.split(".")


						sound_CentersOut.export(dest+"/"+file_name[0]+"_fondo.wav", format="wav")


						#gg  esto  no es perfecto  solo por algunas parte funka xdxdxd 


extraccion_fondo("/home/casey/Escritorio/audio")

