# Bleak-Dash AI

An unofficial [bleak](https://github.com/hbldh/bleak) powered cross-platform Python library for controlling [Wonder Workshop's](https://www.makewonder.com/) [Dash](https://www.makewonder.com/?gclid=CPOO8bC8k8oCFdaRHwodPeMIZg) robot, now with AI chatbot capabilities powered by Google's Gemini models.

This is an enhanced version with AI features available at [https://github.com/sunggeorge/bleak-dash/tree/ai-chat](https://github.com/sunggeorge/bleak-dash/tree/ai-chat).

## Features

- **AI Chatbot Integration**: Interact with Dash using Google's Gemini AI models
- **Voice Recognition**: Speak to Dash and have it understand your commands using speech-to-text
- **Text-to-Speech**: Dash responds verbally to your prompts
- **Dual Input Modes**: Choose between voice or typing to communicate with Dash
- **Cross-Platform Compatibility**: Works on Windows, Mac, and Linux

## Requirements

- Python 3.9 or higher
- Google Gemini API key
- Dash robot (Optional if CONNECT_DASH=False)
- Dash robot MAC address (For quick connection, you can find it using the unforked version.Optional if CONNECT_DASH=False)

## Installation

1. Clone this repository:
   ```
   git clone -b ai-chat https://github.com/sunggeorge/bleak-dash.git
   cd bleak-dash
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key
   - Configure other settings as needed

## Configuration

The application uses the following environment variables (configured in `.env`):

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `GEMINI_MODEL`: The specific Gemini model to use (default: gemini-2.5-pro-preview-03-25)
- `MAC_ADDRESS`: The MAC address of your Dash robot
- `INPUT_MODE`: Choose between "voice" or "typing" for input (default: typing)
- `CONNECT_DASH`: Set to "True" to connect to a physical Dash robot, "False" for text-only mode

## Usage

Run the application:
```
python main.py
```

### Commands:
- Say "bye" or "quit" to exit the application
- Ask questions or give commands to interact with the AI

## Original Project Notice

Adapted from original source code Copyright 2016 Ilya Sukhanov (https://github.com/IlyaSukhanov/morseapi) and updated code Copyright 2018 Russ Buchanan (https://github.com/havnfun/python-dash-robot) with key differences:
- Changed backend from pygatt to bleak
- Compatible with Python 3.11
- Cross Platform
- Asynchronous
- Added AI chatbot capabilities

## License

This project is licensed under the MIT License - see the LICENSE file for details.
