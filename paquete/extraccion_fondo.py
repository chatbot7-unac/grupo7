from pydub import AudioSegment
from pydub.playback import play
import os

 

	
#dest="/home/casey/Escritorio/audio"
#myAudioFile="aud.mp3"
def extraccion_fondo(dest,myAudioFile):

	# read in audio file and get the two mono tracks
	sound_stereo = AudioSegment.from_file(dest+"/"+myAudioFile ,format="mp3")
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


extraccion_fondo("/home/casey/Escritorio/audio","lo_mio.mp3")


