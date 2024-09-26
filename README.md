# Susan - Virtual Assistant
By [@alvarogonmar](https://github.com/alvarogonmar)


**Susan** is a Python-based virtual assistant designed to simplify your daily tasks. Whether you want to check the weather, play your favorite songs on YouTube, search the web, or just hear a joke, Susan is here to help. It integrates voice recognition, web search, and various APIs to offer an intuitive and responsive experience.

## Features
- **Voice Recognition**: Listens and responds to voice commands using `SpeechRecognition`.
- **Voice Output**: Speaks back to the user with natural-sounding voice via `pyttsx3`.
- **Weather Forecasting**: Fetches and tells you the current weather in any city using the OpenWeatherMap API.
- **Web Integration**: Opens YouTube, Google, Netflix, and Max (HBO Max) with simple voice commands.
- **Music and Videos**: Plays songs or videos on YouTube using `pywhatkit`.
- **Jokes**: Lighten your mood with a random joke fetched from `pyjokes`.
- **Time and Date**: Provides current time and date information.
- **Wikipedia Search**: Retrieves quick summaries from Wikipedia for any search query.
- **Internet Search**: Searches the web using `pywhatkit`.
  
## Requirements
To run this project, ensure you have the following installed:

- **Python 3.x**
- **Libraries**:
  ```bash
  pip install pyttsx3 SpeechRecognition pywhatkit yfinance pyjokes wikipedia-api requests python-dotenv
  ```

## Setup
### Clone the repository:
```bash
git clone https://github.com/alvarogonmar/Virtual-Assistant.git
cd Virtual-Assistant
```
### Create a .env file in the project directory and add your OpenWeatherMap API key:
```bash
API_KEY=your_openweathermap_api_key
```

### Run the assistant:
```bash
python virtual_assistant.py
```

## How It Works
- **Listening to Voice Commands**: The assistant uses the microphone to capture audio and convert it into text with Google’s speech recognition API.
- **Natural Responses**: Susan uses `pyttsx3` to respond to user commands with a friendly and natural-sounding voice.
- **Web Search and Entertainment**: Easily open websites like YouTube, Google, Netflix, and Max. You can also play music directly from YouTube or search the web for information.
- **Jokes and Weather**: Susan can tell you jokes or update you on the weather in your city with the OpenWeatherMap API.



