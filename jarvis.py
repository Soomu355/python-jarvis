import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "Hello boss, good morning..... I hope you are having a great day. How can I help you?"
    elif hour >= 12 and hour < 17:
        return "Hello boss, good afternoon........ I hope you are having a great day. How can I help you?"
    elif hour >= 17 and hour < 21:
        return "Hello boss, good evening......... I hope you are having a great day. How can I help you?"
    else:
        return "Hello boss, I hope you are having a good day. How can I help you?"

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en_in')
        print(text)
    except Exception:
        speak("Error")
        print("Error")
        return "none"
    return text

if __name__ == "__main__":
    while True:
        act_com = takecom().lower()
        if "hey jarvis" in act_com or "hi jarvis" in act_com or "hi" in act_com:
            speak(wish())
            query = takecom().lower()

            if "search" in query or "what" in query or "find" in query:
                speak("Searching details... please wait")
                query = query.replace("webbrowser", "")
                result = webbrowser.open(query)
                print(result)
                speak(result)

            elif "calculate" in query:
                speak("Please wait, let me check")
                query = query.replace("calculate", "").strip()
                try:
                    result = eval(query)
                    print(result)
                    speak(f"The result is {result}")
                except Exception as e:
                    speak(f"Sorry, I couldn't perform the calculation. Error: {str(e)}")

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("Finding details for")
                speak(location)
                webbrowser.open(f"https://www.google.nl/maps/place/{location}")

            elif 'date' in query:
                today = datetime.datetime.today()
                d = today.strftime("%B %d, %Y")
                print(d)
                speak(d)

            elif 'time' in query:
                now = datetime.datetime.now()
                d = now.strftime("%H:%M")
                print(d)
                speak(d)

            elif "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "wikipedia" in query:
                speak("Searching details... please wait")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query)
                print(result)
                speak(result)

            elif "youtube" in query:
                query = query.replace("youtube", "")
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")

            elif "open google" in query:
                webbrowser.open("https://www.google.co.in")
                speak("Opening Google")

            elif "play music" in query:
                speak("Okay boss")
                music_dir = "F:\\python\\jarvis project\\music1"  # Change this path if necessary
                if os.path.exists(music_dir):
                    musics = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, musics[0]))  # Play first music file
                else:
                    speak("Music directory not found")

            elif "goodbye" in query:
                speak("Goodbye boss")
                exit()

            else:
                speak("I don't understand what you are saying")

        else:
            print("Invalid activation command")
            speak("Invalid activation command")
