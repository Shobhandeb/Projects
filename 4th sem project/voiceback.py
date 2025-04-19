import pyaudio
import wave
from google.cloud import texttospeech as tts

# Replace with your own Google Cloud credentials file path
credentials_path = '/path/to/credentials.json'

# Define the audio configuration
audio_config = tts.AudioConfig(
    audio_encoding=tts.AudioEncoding.LINEAR16,
    speaking_rate=0.8,
    pitch=5,
    gender=tts.SsmlVoiceGender.FEMALE
)

# Define the Google Text-to-Speech client
client_tts = tts.TextToSpeechClient(credentials=service_account.Credentials.from_service_account_file(credentials_path))

# Define a function to record the user's voice
def record_audio(file_name, duration):
    chunk = 1024  
    sample_format = pyaudio.paInt16  
    channels = 1
    fs = 44100  

    p = pyaudio.PyAudio()  

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  

    for i in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


# Define a function to play the given audio file
def play_audio(file_name):
    wf = wave.open(file_name, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(1024)

    while data:
        stream.write(data)
        data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()

    p.terminate()


# Record the user's voice
record_audio('input.wav', 5)

# Convert the user's voice to a female tone
with open('input.wav', 'rb') as f:
    content = f.read()

    synthesis_input = tts.SynthesisInput(audio=content)

    voice = tts.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-D',
        ssml_gender=tts.SsmlVoiceGender.FEMALE
    )

    response = client_tts.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open('output.wav', 'wb') as out:
        out.write(response.audio_content)

# Play back the converted voice
play_audio('output.wav')
