from pydub import AudioSegment
import wave
from pydub.utils import make_chunks
import os
import sox
from prob import *

def problem1(dest,v,ml):
	convert(dest)
	ruido(dest)
	velocidad(dest,v)
	particion(dest,ml)





#problem1("/home/casey/Escritorio/bd/",2,30000)



	