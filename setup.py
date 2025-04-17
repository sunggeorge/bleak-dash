from setuptools import setup, find_packages

setup(
    name='bleak-dash',
    version='0.2.0',  # Increment version for your significant additions
    author='Alex Klein',
    author_email='alexanderjamesklein@gmail.com',
    description='An unofficial bleak powered library for controlling Wonder Workshop\'s Dash robot with added AI chatbot capabilities.',
    long_description="""
# bleak-dash

An unofficial [bleak](https://github.com/hbldh/bleak) powered cross-platform Python library for controlling [Wonder Workshop's](https://www.makewonder.com/) [Dash](https://www.makewonder.com/?gclid=CPOO8bC8k8oCFdaRHwodPeMIZg) robot.

## NOTICE
Adapted from original source code Copyright 2016 Ilya Sukhanov (https://github.com/IlyaSukhanov/morseapi) and updated code Copyright 2018 Russ Buchanan (https://github.com/havnfun/python-dash-robot) with key differences:
- Changed backend from pygatt to bleak
- Compatible with Python 3.11
- Cross Platform
- Asynchronous

## New Features
- AI chatbot integration using Google's Gemini models
- Voice recognition and text-to-speech capabilities
- Interactive robot movements synchronized with AI responses

## Motivation
Designed for use with Dash robot from various operating systems without reinventing the wheel, now with added AI conversation capabilities.

## Compatibility
Thanks to Bleak, the library is Windows, Mac, and Linux agnostic. Tested on M1 & Windows.
""",
    long_description_content_type='text/markdown',
    url='https://github.com/mewmix/bleak-dash',
    packages=find_packages(),
    install_requires=[
        'bleak==0.21.1',
        'colour==0.1.5',
        'google-generativeai>=0.3.2',
        'SpeechRecognition>=3.10.0',
        'gTTS>=2.5.4',
        'playsound>=1.2.2',
        'python-dotenv>=1.0.0',
        'PyAudio>=0.2.14',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='bleak dash robot wonder workshop asynchronous ai chatbot gemini speech',
    python_requires='>=3.9',
)