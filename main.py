from google.cloud import texttospeech
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i',dest='input')
parser.add_argument('-o',dest='output')
args = parser.parse_args()

if args.input is None or args.output is None:
    print("Input and output need to be supplied")
    sys.exit()

sys.exit()
client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.types.SynthesisInput(text="Hi")

voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3
)

response = client.synthesize_speech(synthesis_input,voice,audio_config)

with open('output.mp3','wb') as out:
    out.write(response.audio_content)