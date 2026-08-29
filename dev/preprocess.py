import subprocess

#Manage GPU processes
from fairseq2 import gang
gang._thread_local.current_gangs = []

#Manage audio input into .wav format
def encode_audio(audio):
    # 'audio' is the file name and its extension
    encoded_audio = subprocess.run(
        ['ffmpeg', '-i', audio, '-f', 'wav', 'pipe:1'],
        check= True,
        capture_output= True
    )
    return encoded_audio

#Break down audio into small segments
#That will fade in and out of each other, with overlaps
def segment_audio():
    
