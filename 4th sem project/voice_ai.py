
# allow us to asces the gpt 3 api 
import openai
#text to speech convert 
import pyttsx3
#speech to text convert 
import speech_recognition as sr
import time 

#set your OpenAI  API  key 
openai.api_key=""

#initialize the text to sppech engine 
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skiping unknown error ')


def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n=1,
        stop = None,
        temperature = 0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        #wait for user to say hi 
        print("Say 'hi' to start recording your question ")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() =="hi":
                    #record audio
                    filename = "input.way"
                    print("Say your question ...")
                    with sr.Microphone() as source:
                        recognizer = sr.recognizer()
                        source.pause_threshold = 1 
                        audio = recognizer.listen(source , phrase_time_limit=None , timeout=None)
                        with open(filename,"wb") as f:
                            f.write(audio.get_wav_data())

                    #Transcibe audio to text 
                    text =transcribe_audio_to_text(filename)
                    if text:
                        print(f"you said : {text}")

                        #Generate response using GPT 3 
                        response = generate_response(text)
                        print(f"GPT-03 says : {response}")

                        #read response using text to speech 
                        speak_text(response)
            except Exception as e:
                print("An error occured :{}".format(e))


if __name__ == "_main_":
    main()