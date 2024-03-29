import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Evening!")

    else:
        speak("Good Evenging!")

    speak("I am Friday Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print("e")
        print("say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        sites = [["youtube", "youtube.com"], [
            "google", "google.com"], ["stackoverflow", ""]]

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        for site in sites:
            if f"Open {site[0]}" in query:
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        #   elif 'open youtube' in query:
        #       webbrowser.open("youtube.com")

        #   elif 'open google' in query:
        #       webbrowser.open("google.com")

        #   elif 'open stackoverflow' in query:
        #        webbrowser.open("stackoverflow.com")
        if "the time " in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strfTime}")
        #   elif 'play music' in query:
        #        music_dic = "C:\Users\KIIT\Videos\Captures"
        #        songs = os.listdir(music_dir)
        #        print(songs)
        #        os.startfile(os.path.join(music_dir , songs[0]))
