import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Improve recognition
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

newsapi = "dccb792d82034e8399e97c4246adc1f4"


# 🔹 Speak function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# 🔹 Record audio (no PyAudio)
def record_audio(duration=2, fs=16000):
    print("Listening... Speak now")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Convert float → int16 (IMPORTANT)
    audio = (audio * 32767).astype('int16')

    return np.squeeze(audio), fs


# 🔹 Convert audio → text
def listen_command(duration=2):
    audio_data, fs = record_audio(duration)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            wav.write(f.name, fs, audio_data)

            with sr.AudioFile(f.name) as source:
                audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""

    except sr.RequestError:
        print("❌ Internet issue (Google API)")
        return ""

    except Exception as e:
        print("❌ Error:", e)
        return ""


# 🔹 Command processor
def processCommand(c):
    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = " ".join(c.split(" ")[1:])
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")

    elif "news" in c:
        try:
            print("Fetching news...")
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=dccb792d82034e8399e97c4246adc1f4"
            )
          
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])

                for article in articles[:5]:
                    speak(article['title'])
            else:
                speak("Failed to fetch news")

        except Exception as e:
            print(e)
            speak("Error fetching news")


# 🔹 Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            print("\nSay 'Jarvis'...")
            word = listen_command(4)

            if "jarvis" in word:
                speak("Yes")

                print("Listening for command...")
                command = listen_command(5)

                if command:
                    processCommand(command)
                else:
                    speak("I did not catch that")

        except Exception as e:
            print("Error:", e)