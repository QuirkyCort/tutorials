# Audio Classifier

This tutorial will show you how to train an audio classifier using Teachable Machine, then write Python code to detect the trained audio.

You can use it for various purposes, such as...

* Send voice commands to a robot
* Detect audio alarms
* Recognize animals from their sound

Note that when using Teachable Machines, audio samples are limited to 1 second each, so you can't have long commands.
If you need longer commands (eg. "turn left"), you can break them into multiple classes (ie. one for "turn", another for "left") and detect if the two classes appear consecutively.

## Training

1. Open the [Teachable Machine](https://teachablemachine.withgoogle.com/) website.
2. Click "Get Started"
3. Select "Audio Project"
4. Record your background noise then click "Extract Sample".
5. Record your audio sample. Note that this will record for two seconds by default, if recording a word, you should say it twice. Click "Extract Sample" after each recording.
6. Add a new class and repeat the sample recording if needed.
7. When you have sufficient samples, click "Train Model" and wait for it to complete.
8. Click "Export Model", select "TensorFlow Lite", then download the model.

You should now have a zip file named "converted_tflite.zip".
Open it up and extract the file named "soundclassifier_with_metadata.tflite"; this file contains the trained weights.

## Installation

To run an audio classifier on Python, you'll need to install a few things.

### LiteRT

This is the software library for machine learning.
LiteRT (...formerly known as TensorFlow Lite) provides a lighter (smaller install size, lower memory use) alternative to TensorFlow.
If you already have TensorFlow installed, you can use that instead.

To install LiteRT on Linux systems (...including Raspberry Pi), first create and activate a new virtual environment...

```
python -m venv litert
source litert/bin/activate
```
On Mac and Windows, you can skip the above step.
Next, you'll need to install LiteRT...

```
pip install ai-edge-litert
```

### MediaPipe

MediaPipe provides machine learning models for various tasks.
We'll be using the Audio Classifier model provided by MediaPipe.

```
pip install mediapipe
```

## Code

```python
import time

from mediapipe.tasks import python
from mediapipe.tasks.python.audio.core import audio_record
from mediapipe.tasks.python.components import containers
from mediapipe.tasks.python import audio

import numpy as np

# Various options. You can play around with these.
model = 'soundclassifier_with_metadata.tflite'
max_results = 5
score_threshold = 0.8
overlapping_factor = 0.5


# Callback function. The audio classifier will run this after classification.
def print_result(result, timestamp_ms):
    if len(result.classifications[0].categories) < 1:
        return

    first_result = result.classifications[0].categories[0]

    # Only print if the detected audio is not the background noise.
    if first_result.category_name[0] != '0':
        print(first_result)

# Initialize the audio classification model.
base_options = python.BaseOptions(model_asset_path=model)
options = audio.AudioClassifierOptions(
    base_options=base_options, running_mode=audio.RunningMode.AUDIO_STREAM,
    max_results=max_results, score_threshold=score_threshold,
    result_callback=print_result)
classifier = audio.AudioClassifier.create_from_options(options)

# Initialize the audio recorder
buffer_size, sample_rate, num_channels = 44100, 44100, 1
record = audio_record.AudioRecord(num_channels, sample_rate, buffer_size)

# Initialize a tensor to store the audio data
audio_format = containers.AudioDataFormat(num_channels, sample_rate)
audio_data = containers.AudioData(buffer_size, audio_format)

# We'll try to run inference every interval_between_inference seconds.
# This is usually half of the model's input length to create an overlapping
# between incoming audio segments to improve classification accuracy.
input_length_in_second = buffer_size / sample_rate
interval_between_inference = input_length_in_second * (1 - overlapping_factor)
last_inference_time = time.time()

# Start audio recording in the background.
record.start_recording()

# Loop forever
while True:
  # Wait until at least interval_between_inference seconds has passed since
  # the last inference.
  now = time.time()
  diff = now - last_inference_time
  if diff < interval_between_inference:
    time.sleep(0.01)
    continue
  last_inference_time = now

  # Load the input audio from the AudioRecord instance and run classify.
  data = record.read(buffer_size)
  audio_data.load_from_array(data.astype(np.float32))
  classifier.classify_async(audio_data, time.time_ns() // 1_000_000)
```

Save the above code into a .py file (eg. audio.py), and run it with...

```
python audio.py
```

Say the word that you have used for training; you should see the result printed on screen.
You may also see some warning messages (...mostly related to timestamp), and can safely ignore them.
