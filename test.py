import pyttsx3


### 0.SETTING Voicer
engine = pyttsx3.init()

### 1.Config Speed and volume

#### 1.1 Speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-130)

#### 1.2 Volume
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)

#### 1.3 Change Voice man or woman
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# for value in voices :
#     print(value)

def speech_vie_data(text) :
    engine.say(text)
    engine.runAndWait()