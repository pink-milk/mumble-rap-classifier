from google.cloud import speech_v1 as speech
# from google.cloud.speech import enums
import os
import io

# Creates google client
client = speech.SpeechClient()
song_file="soccermom_trimmed.flac"
# Full path of the audio file, Replace with your file name
file_name = os.path.join(os.path.dirname(__file__),song_file)

#Loads the audio file into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    # encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
    audio_channel_count=2,
    language_code="en-US",
)

# Sends the request to google to transcribe the audio
response = client.recognize(request={"config": config, "audio": audio})

# Reads the response

for result in response.results:
    print("{}".format(result.alternatives[0].transcript))

a_file = open("soccermom.txt", "w")

# for result in response.results:
# a_file.writelines(response.transcript)

for result in response.results:
    a_file.write("{}".format(result.alternatives[0].transcript))
a_file.close()


#Ffmpeg, Acapella extractor, Mp3cut.net, Python (Matplotlib, Seaborn, nltk, SoundEx, SciPy, PyDub, NumPy, Pandas) and Power BI.

#1) download .mp3
#2) input into acapella extractor
#3) trim file
#4) convert to flav file
#5) input into program
