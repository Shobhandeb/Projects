import os
import time

from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech as tts
from google.oauth2 import service_account
import pyaudio
import pygame


# Replace with your own Google Cloud credentials file path
credentials_path = '/path/to/credentials.json'

# Define the audio configuration
audio_config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
    model='phone_call',
    use_enhanced=True,
    enable_automatic_punctuation=True,
    diarization_config=speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=1,
        max_speaker_count=2
    ),
)

# Define the Google Text-to-Speech client
client_tts = tts.TextToSpeechClient(credentials=service_account.Credentials.from_service_account_file(credentials_path))

# Define the Google Speech-to-Text client
client_stt = speech.SpeechClient(credentials=service_account.Credentials.from_service_account_file(credentials_path))


# Define a function to play the given text as audio
def speak(text):
    synthesis_input = tts.SynthesisInput(text=text)

    voice = tts.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-D',
        ssml_gender=tts.SsmlVoiceGender.FEMALE
    )

    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16
    )

    response = client_tts.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open('output.wav', 'wb') as out:
        out.write(response.audio_content)

    pygame.mixer.init()
    pygame.mixer.music.load('output.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove('output.wav')


# Define a function to recognize speech and return the text
def recognize_speech():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    print("Listening...")

    frames = []
    start_time = time.time()

    while True:
        data = stream.read(1024)
        frames.append(data)
        elapsed_time = time.time() - start_time

        if elapsed_time > 5.0:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio = speech.RecognitionAudio(content=b''.join(frames))
    response = client_stt.recognize(config=audio_config, audio=audio)

    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript.strip()


# Define the main function
def main():
    while True:
        try:
            query = recognize_speech()
            print(f"You said: {query}")

            if 'hello' in query:
                speak("Hello! How can I assist you?")

            elif 'bye' in query:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I don't understand. Please try again.")

        except Exception as e:
            print(e)
            speak("Sorry, there was an error. Please try again.")


if __name__ == '__main__':
    main()

