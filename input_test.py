from speech_lib import *
from random import randint


#### Phép cộng


# for i in range(0,10):
#     a_random = randint(1,10)
#     b_random = randint(3,20)
#     a_array_test.append(a_random)
#     b_array_test.append(b_random)
#
# input_test(a_array_test,b_array_test,'+')
#
#
# #### Phép nhân'


speech_vie_data('Bài test phép cộng trong phạm vi 100')
input_test_plus(10,[1,99],[1,9],'+')

speech_vie_data('Bài test phép trừ trong phạm vi 100')
input_test_plus(5,[1,9],[1,99],'-')

speech_vie_data('Bài test phép nhân')
input_test_plus(10,[1,99],[1,9],'+')

speech_vie_data('Bài test phép chia')
input_test_plus(5,[1,9],[1,9],':')