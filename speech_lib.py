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



def input_test(a_array,b_array,type):
    len_array = len(a_array)
    correct_count  = incorect_count = total_count   = 0


    for i in range(0,len_array):
        a_value = a_array[i]
        b_value = b_array[i]
        question_show = f'{a_value} {type} {b_value} = ? '
        if type == '+':
            type_name = 'cộng'
            correct = a_value + b_value
        elif type == '-':
            type_name = 'trừ'
            correct = a_value - b_value
        elif type == 'x':
            type_name = 'nhân'
            correct = a_value * b_value
        elif type == ':':
            type_name = 'chia'
            correct = a_value / b_value
        question_name = f'{a_value} {type_name} {b_value} bằng bao nhiêu'

        ### Show question
        print(question_show)
        speech_vie_data(question_name)
        answer = int(input('Kết quả : '))
        if answer == correct :
            result = 'Đúng'
            speech_vie_data('Đúng rồi')
            correct_count+=1
        else :
            result = 'Sai'
            speech_vie_data('Sai rồi')
            incorect_count+=1
        total_count+= 1

    correct_rate = correct_count / total_count * 100
    incorrect_rate = incorect_count / total_count * 100
    print(f'Tỷ lệ câu đúng là {correct_rate}%:')
    speech_vie_data(f'Tỷ lệ câu đúng là {correct_rate}%:')
    print(f'Tỷ lệ câu sai là {incorrect_rate}%:')
    speech_vie_data(f'Tỷ lệ câu sai là {incorrect_rate}%:')







# data_read_test = read_local('list_speech_test/match_speech_test.txt')
# print(data_read_test)
# speech_vie_data('1cm bằng 10 mm')