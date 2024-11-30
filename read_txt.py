import codecs
import os

folder_url = 'list_text'
list_file  = os.listdir(folder_url)
print(list_file)

#### SELECT File name
index = int(input('Nhap so tt :'))
file_name = list_file[index]
file_url  = folder_url + '/' + file_name
print(file_url)


from test import speech_vie_data
from time import sleep
local_file = file_url
with codecs.open(local_file, encoding='utf-8') as f:
    for line in f:
        print(line)
        for i in range (0,5):
            speech_vie_data(line)
            sleep(1)
        sleep(2)
    speech_vie_data('hết bài')