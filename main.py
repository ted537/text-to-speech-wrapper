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

with open(args.input,'r') as input_file:
    lines = input_file.readlines()
    input_str = ''.join(lines)

client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.types.SynthesisInput(text=input_str)

voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3
)

response = client.synthesize_speech(synthesis_input,voice,audio_config)

with open(args.output,'wb') as out:
    out.write(response.audio_content)