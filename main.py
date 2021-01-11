import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()

with sr.Microphone() as source:
    print('[search edureka: search video: search write]')
    print('----SPEAK NOW----')
    audio = r.listen(source)

if 'edureka' in r.recognize_google(audio):
    r = sr.Recognizer()
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('---SEARCH YOUR QUERY---')
        audio = r.listen(source)

        try:
            get = r.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('ERROR!')
        except sr.RequestError as e:
            print('FAILED'.format(e))

elif 'video' in r.recognize_google(audio):
    r = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('---SEARCH YOUR QUERY---')
        audio = r.listen(source)

        try:
            get = r.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('ERROR!')
        except sr.RequestError as e:
            print('FAILED'.format(e))

else:
    r = sr.Recognizer()
    def initSpeech():
        print("LISTENING......")

        with sr.Microphone() as source:
            print("--PLEASE SAY SOMETHING")
            audio = r.listen(source)

        command = ""

        try:
            command = r.recognize_google(audio)
        except:
            print("!!CAN'T HEAR YOU!!")

        print("YOUR COMMAND: ")
        print(command)


    initSpeech()