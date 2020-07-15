#open-cmd

#pip install gTTS

#gTTS - google text to speech

from gtts import gTTS

tts = gTTS('Om Ganeshaya Namaha')

#tts - text to speech
#Om Ganeshaya Namaha - Text

tts.save('Om.mp3')

#om.mp3 - om(file name) 
#mp3(to save text as song)