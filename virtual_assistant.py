import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import requests
from dotenv import load_dotenv
import os
#VOICE
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#API KEY OpenWeatherMap
load_dotenv()
api_key = os.getenv('API_KEY')


#LISTEN MICROPHONE, RETURNING THE AUDIO AS TEXT
def transform_audio_as_text():

    # STORE RECOGNIZER IN A VARIABLE
    r = sr.Recognizer()

    #SET UP THE MICROPHONE
    with sr.Microphone() as origin:

        #WAITING TIME
        r.pause_threshold = 0.8

        #REPORT THAT THE RECORDING STARTED
        print('You can talk now')

        #SAVE WHAT THE USER SAID AS AUDIO
        audio = r.listen(origin)

        try:
            #SEARCH IN GOOGLE 
            order = r.recognize_google(audio, language='en-us')

            #WHAT THE USER SAID
            print(f'You said:  {order}')

            #RETURN ORDER
            return order
        
        #IN CASE THAT THE 'VA' DOESN'T UNDERSTAND THE AUDIO
        except sr.UnknownValueError:

            #TEXT IN CASE THE AUDIO WAS NOT UNDERSTOOD
            print('Ups, I didnt understand')

            #RETURN ERROR
            return 'Waiting...'
        
        #IN CASE THAT THE ORDER CANT BE RESOLVED

        except sr.RequestError:

            #TEXT IN CASE THE AUDIO WAS NOT UNDERSTOOD
            print('Ups, I didnt understand')

            #RETURN ERROR
            return 'Waiting...'
        
        #UNEXPECTED ERROR 
        except:
            #TEXT IN CASE THE AUDIO WAS NOT UNDERSTOOD
            print('Ups, something went wrong')

            #RETURN ERROR
            return 'Waiting...'
        
# FUNCTION: VIRTUAL ASSISTANT CAN BE HEARD BY THE USER
def talk(message):

    # TURN ON PYTTSX3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #SAY MESSAGE
    engine.say(message)
    engine.runAndWait()

#INFORM THE DAY OF THE WEEK
def ask_day():

    #VARIABLE WITH THE DAY
    day = datetime.date.today()
    print(day)

    #VARIABLE WITH THE DAY OF THE WEEK
    day_week = day.weekday()
    print(day_week)

    #DICTIONARY WITH THE NAME OF THE DAYS
    calendar = {0: 'Monday',
                  1: 'Tuesday',
                  2: 'Wednesday',
                  3: 'Thursday',
                  4: 'Friday',
                  5: 'Saturday',
                  6: 'Sunday'}
    
    #SAY THE DAY OF THE WEEK
    talk(f'Today is {calendar[day_week]}')


#INFORM THE HOUR
def ask_hour():
    
    #VARIABLE WITH THE DATAS OF THE HOUR
    hour = datetime.datetime.now()
    hour = f'Its {hour.hour} hours with {hour.minute} minutes and {hour.second} seconds'
    print(hour)

    #SAY THE HOUR
    talk(hour)

#FUNTION: INITIAL GREETING
def initial_greeting():

    #VARIABLE WITH THE DATAS OF THE HOUR
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour >20:
        moment = 'Good night'
    elif  6 <= hour.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'

    #SAY GREETING
    talk(f'{moment}, Its me, Susan, your personal assistant. Please tell me how can I help you')


def ask_weather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'appid=' + api_key + '&q=' + city + '&units=metric'
    response = requests.get(complete_url)
    data = response.json()
    if data['cod'] != '404':
        main = data['main']
        temperature = main['temp']
        weather_desc = data['weather'][0]['description']
        return f'The temperature in {city} is {temperature} degrees Celsius with {weather_desc}.'
    else:
        return 'City not found.'

#CENTRAL FUNCTION OF THE ASSISTANT
def ask_things():
    
    #ACTIVE INITIAL GREETING
    initial_greeting()

    #VARIABLE OF CUT
    comenzar = True
    
    #CENTRAL LOOP
    while comenzar:

    #ACTIVATE MICROPHONE AND SAVE THE ORDER IN A STRING
        order = transform_audio_as_text().lower()

        if 'open youtube' in order:
            talk('Sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open google' in order:
            talk('Of course, I am opening google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what\'s the date' in order:
            ask_day()
            continue
        elif 'what\'s the hour' in order or 'what time is it' in order:
            ask_hour()
            continue
        elif 'search on wikipedia' in order:
            try:
                order = order.replace('search on wikipedia', '').strip()
                talk(f'Searching {order}')
                if order:
                    wikipedia.set_lang('en')
                    result = wikipedia.summary(order, sentences=1)
                    talk(f'This is what I found in wikipedia: {result}')
                else:
                    talk('Please, tell me what you want to search on wikipedia')
            except wikipedia.exceptions.DisambiguationError as e:
                talk('Please, tell me what you want to search on wikipedia')
            except wikipedia.exceptions.PageError:
                talk('I didn\'t find any website for that search')
            except:
                talk('Ups, something went wrong')
            continue
        elif 'search on the internet' in order:
            order = order.replace('search on the internet', '')
            talk(f'Searching  {order}')
            pywhatkit.search(order)
            talk('This is what I found on the internet')
            continue
        elif 'play' in order:
            try:
                order = order.replace('play', '')
                talk(f'Playing  {order}')
                if order:
                    pywhatkit.playonyt(order)
                else:
                    talk('Please, tell me what you want to play')
            except:
                talk('Please, tell me what you want to play')
            continue
        elif 'joke' in order:
            talk(pyjokes.get_joke('en'))
            continue
        elif 'tell me the weather in' in order or 'what\'s the weather in':
            try:
                city = order.replace('tell me the weather in', '').strip()
                weather_info = ask_weather(city)
                talk(weather_info)
            except:
                talk('Sorry, I could not retrieve the weather information.')
            continue
        elif 'open max' in order or 'open hbo max' in order:
            talk('Sure, I am opening max')
            webbrowser.open('https://play.max.com/')
            continue
        elif 'open netflix' in order:
            talk('Sure, I am opening Netflix')
            webbrowser.open('https://www.netflix.com/mx/')
            continue
        elif 'bye' in order:
            talk('My pleasure, Im here to help you')
            break


ask_things()