import os
import time
import threading
import speech_recognition as sr
from gtts import gTTS
import playsound
import tempfile
import google.generativeai as genai
from dotenv import load_dotenv
from dash.chatbot import Chatbot
import asyncio

# Load environment variables
load_dotenv(override=True)  # Force reload with override=True
INPUT_MODE = os.getenv("INPUT_MODE", "voice")  # Default to voice input
# Convert string "True"/"False" to boolean True/False
CONNECT_DASH = os.getenv("CONNECT_DASH", "False").lower() == "true"

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

OUTPUT_DEVICE_ID = int(os.getenv("OUTPUT_DEVICE_ID", 5))  # Default to device 5

# Initialize Google Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

# Initialize STT recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# State flags
is_processing = False
is_waiting_for_ai = False
is_responding = False

# Processing icon
def display_processing_icon(state):
    if state:
        print("🔄 Processing...")
    else:
        print("✅ Ready")

# Function to listen and transcribe speech
def listen_and_transcribe():
    global is_processing, is_waiting_for_ai, is_responding

    with microphone as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("🔍 Transcribing...")
        text = recognizer.recognize_sphinx(audio)
        print(f"👤 User said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError as e:
        print("❌ Speech recognition service failed")
        return None

# Function to interact with Gemini AI
def chat_with_gemini(prompt):
    global is_waiting_for_ai

    is_waiting_for_ai = True
    display_processing_icon(True)

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Error communicating with Gemini AI: {e}")
        return None
    finally:
        is_waiting_for_ai = False
        display_processing_icon(False)

# Function to speak the AI response using gTTS and playsound
def speak_response(text):
    global is_responding

    is_responding = True
    display_processing_icon(True)

    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
        tts.save(temp_path)
        playsound.playsound(temp_path)
        os.remove(temp_path)
    except Exception as e:
        print(f"❌ Error during TTS: {e}")
    finally:
        is_responding = False
        display_processing_icon(False)

# Main loop
async def main():
    global is_processing, is_waiting_for_ai, is_responding

    # Initial system prompt
    system_prompt = "You are a clever and friendly bot called Dash. You reply up to one or two sentences."
    
    if CONNECT_DASH:
        print("🤖 Chatbot is starting...")
        try:
            MAC_ADDRESS = os.getenv("MAC_ADDRESS")
            mybot = Chatbot(MAC_ADDRESS)
            print("🤖 Initializing Chatbot...")
            await mybot.connect()
            print("🤖 Chatbot connected.")
            # print("AI initialization status: {0}", chat_with_gemini(system_prompt))
        except Exception as e:
            print(f"❌ Error initializing Chatbot: {e}")
            return

    while True:
        if not (is_processing or is_waiting_for_ai or is_responding):
            is_processing = True
            display_processing_icon(True)
            
        # Listen and transcribe, based on input mode
        if INPUT_MODE.lower() == "typing":
            user_input = input("Type your message: ")
        else:
            user_input = listen_and_transcribe()

        if user_input:
            if user_input == "bye" or user_input == "quit":
                if CONNECT_DASH:
                    await mybot.disconnect()
                print("👋 Goodbye!")
                break
            else:
                # Send to Gemini AI
                ai_response = chat_with_gemini(system_prompt + user_input)

                if ai_response:
                    print(f"🤖 AI message: {ai_response}")
                    
                    if CONNECT_DASH:
                        await mybot.say_action()
                    
                    # Speak the response
                    speak_response(ai_response)

            is_processing = False
            display_processing_icon(False)

            time.sleep(0.1)  # Small delay to avoid busy-waiting

if __name__ == "__main__":
    asyncio.run(main())