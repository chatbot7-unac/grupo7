from pydub import AudioSegment
import wave
from pydub.utils import make_chunks
import os
import sox

UPLOAD_FOLDER = '/home/casey/Escritorio/bd/'
def convert():
	for archivo in os.listdir(UPLOAD_FOLDER):
			name_file=archivo.split('.')
			if(name_file[1]=='mp3'):
				sound=AudioSegment.from_mp3(UPLOAD_FOLDER+archivo)
				sound.export(UPLOAD_FOLDER+name_file[0]+".wav",format="wav")

"""
def convert(UPLOAD_FOLDER,file):
	os.system("sox "+UPLOAD_FOLDER+"/"+file+" -r 16000 -c 1 -b 16 "+UPLOAD_FOLDER+"filename.wav")
"""