import codecs
import pyttsx3

def read_local(file_url):
    data_read = []
    with codecs.open(file_url, encoding='utf-8') as f:
        for line in f:
            line = line.replace('\r\n','')
            data_read.append(line)
    return data_read






### 0.SETTING Voicer
engine = pyttsx3.init()
#### 1.1 Speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-110)

#### 1.2 Volume
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)

#### 1.3 Change Voice man or woman
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# for value in voices :
#     print(value)

def speech_vie_data(text):
    engine.say(text)
    engine.runAndWait()

# data_read_test = read_local('list_speech_test/match_speech_test.txt')
# print(data_read_test)
# speech_vie_data('1cm bằng 10 mm')