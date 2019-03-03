import speech_recognition as sr
import webbrowser
recognize = sr.Recognizer()
with sr.Microphone() as listen:
    text = 'none'
    print 'What can I search for you?'
    print 'Listening.......'
    gotcha = recognize.listen(listen)
    try:
        text = recognize.recognize_google(gotcha)
        print text
        webbrowser.open("https://www.youtube.com/results?search_query="+text)

    except:
        print 'Please Speak Clearly! '
