# Speech Recognition (Offline)

This tutorial will show you how to read audio from a microphone and convert it into text.
All of the methods shown here are **Offline** methods, which means that you don't need internet access to run them.
Other methods (eg. Google Cloud Speech API) may give better results, but requires an internet connection to work.

We will demonstrate using two different libraries [CMUSphinx / PocketSphinx](https://cmusphinx.github.io/) and [Vosk](https://alphacephei.com/vosk/).
From my (...very limited) tests, Vosk appears to give better results while PocketSphinx uses less memory.

You can use it for various purposes, such as...

* Send voice commands to a robot

Note that if you wish to detect only a few short commands (eg. "left", "right", "up", "down"), you might get better results by training your own audio classifier.

## Installation (CMUSphinx / PocketSphinx)

To install PocketSphinx on Linux systems (...including Raspberry Pi), first create and activate a new virtual environment...

```
python -m venv speech
source speech/bin/activate
```

On Mac and Windows, you can skip the above step.
Next, you'll need to install PocketSphinx and (optionally) PyAudio...

```
pip install pocketsphinx
pip install pyaudio
```

PyAudio is not needed if you are only using the simple code example.

## Simple Code (CMUSphinx / PocketSphinx)

The code for using pocketsphinx can be incredibly simple...

```python
from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print(phrase)
```

...but this simple code have a number of drawbacks, including...

* Not able to select which microphone to use
* Blocking loop; your program can't do other work while waiting for speech
* No configuration options available

Save the above code into a .py file (eg. speech_sphinx.py), and run it with...

```
python speech_sphinx.py
```

Say something, and you should see the words printed on screen.
If no words are printed, check the microphone setting on your computer; it might be turned off.
Note that the Raspberry Pi do not have a built-in microphone; you must add a USB microphone.

## Advanced Code (CMUSphinx / PocketSphinx)

The advanced code for using pocketsphinx provides more features at the expense of a slightly more complicated code.

```python
from pocketsphinx import Endpointer, Decoder
import pyaudio

# Initialize audio
DEVICE = None  # Use default input device
CHUNK = 480  # Size of each audio buffer chunk
FORMAT = pyaudio.paInt16  # Audio format (16-bit signed integer)
CHANNELS = 1  # Mono recording
RATE = 16000  # Sample rate (samples per second)

p = pyaudio.PyAudio()
stream = p.open(input_device_index=DEVICE,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Initialize speech decoder
ep = Endpointer(sample_rate=RATE)
decoder = Decoder(samprate=RATE)

while True:
    data = stream.read(CHUNK, exception_on_overflow = False)
    prev_in_speech = ep.in_speech
    speech = ep.process(data)
    if speech is not None:
        if not prev_in_speech:
            decoder.start_utt()
        decoder.process_raw(speech)
        hyp = decoder.hyp()
        if hyp is not None:
            print("PARTIAL:", hyp.hypstr)
        if not ep.in_speech:
            decoder.end_utt()
            print("FULL:", decoder.hyp().hypstr)
```

Save the above code into a .py file (eg. speech_sphinx.py), and run it with...

```
python speech_sphinx.py
```

Say something, and you should see the words printed on screen.
If no words are printed, check the microphone setting on your computer; it might be turned off.
Note that the Raspberry Pi do not have a built-in microphone; you must add a USB microphone.

## Installation (Vosk)

To install Vosk on Linux systems (...including Raspberry Pi), first create and activate a new virtual environment...

```
python -m venv speech
source speech/bin/activate
```

On Mac and Windows, you can skip the above step.
Next, you'll need to install PyAudio and Vosk...


```
pip install pyaudio
pip install vosk
```

You will also need to download a model from [here](https://alphacephei.com/vosk/models).
This will give you a zip file that you will then need to extract.
In the example code below, we are using the *vosk-model-small-en-us-0.15* model.

## Code (Vosk)

The code for using Vosk is as follows...

```python
import pyaudio
import json
from vosk import Model, KaldiRecognizer

# Model should be stored in this directory
# Change this if you are using a different model or if your model is stored
# in a different directory.
model = Model('vosk-model-small-en-us-0.15')

# Initialize audio
DEVICE = None  # Use default input device
CHUNK = 1024  # Size of each audio buffer chunk
FORMAT = pyaudio.paInt16  # Audio format (16-bit signed integer)
CHANNELS = 1  # Mono recording
RATE = 44100  # Sample rate (samples per second)

p = pyaudio.PyAudio()
stream = p.open(input_device_index=DEVICE,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Main loop
rec = KaldiRecognizer(model, RATE)
while True:
    data = stream.read(CHUNK, exception_on_overflow = False)
    if rec.AcceptWaveform(data): # Returns True when the sentence is complete
        result = json.loads(rec.Result())
        if result['text']:
            print('FULL:', result['text'])
    else: # Partial sentence. You can skip this if you only want full sentences
        result = json.loads(rec.PartialResult())
        if result['partial']:
            print('PARTIAL:', result['partial'])
```

Save the above code into a .py file (eg. speech_vosk.py), and run it with...

```
python speech_vosk.py
```

Say something, and you should see the words printed on screen.
If no words are printed, check the microphone setting on your computer; it might be turned off.
Note that the Raspberry Pi do not have a built-in microphone; you must add a USB microphone.

## Selecting Audio Input Device

The above code uses the default audio device for input (`DEVICE = None`), but this may not always be the best option (eg. you have more than one microphone).
To determine the device number to use when selecting an audio device, you can use this code...

```python
import pyaudio

# Initialize pyaudio
p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(info)
```

This should print the index and info of every available audio device on your system.