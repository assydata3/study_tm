from speech_lib import *
from time import sleep


match_question_url = 'list_speech_test/match_speech_test.txt'
match_question = read_local(match_question_url)
for question in match_question :
    print(question)
    for i in range(0,2):
      speech_vie_data(question)
      sleep(2)
    sleep(5)