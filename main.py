from google.cloud import texttospeech
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i',dest='input')
parser.add_argument('-o',dest='output')
# gender is MALE,FEMALE, or NEUTRAL
parser.add_argument('-g',dest='gender',type=str)
# language code is en-US,en-UK,etc
# https://cloud.google.com/text-to-speech/docs/voices
parser.add_argument('-l',dest='language',type=str)
args = parser.parse_args()

if args.input is None or args.output is None or args.gender is None or args.language is None:
    print("MISSING ARGUMENTS")
    sys.exit()

with open(args.input,'r') as input_file:
    lines = input_file.readlines()
    input_str = ''.join(lines)

client = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.types.SynthesisInput(text=input_str)

voice = texttospeech.types.VoiceSelectionParams(
    language_code=args.language,
    ssml_gender=texttospeech.enums.SsmlVoiceGender[args.gender.upper()]
)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3
)

response = client.synthesize_speech(synthesis_input,voice,audio_config)

with open(args.output,'wb') as out:
    out.write(response.audio_content)