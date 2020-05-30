from google.cloud import texttospeech

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