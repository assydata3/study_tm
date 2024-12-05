from speech_lib import *
from random import randint


#### Phép cộng
a_array_test = []
b_array_test = []

# for i in range(0,10):
#     a_random = randint(1,10)
#     b_random = randint(3,20)
#     a_array_test.append(a_random)
#     b_array_test.append(b_random)
#
# input_test(a_array_test,b_array_test,'+')
#
#
# #### Phép nhân
a_array_mutil_test = []
b_array_mutil_test = []

for i in range(0,10):
    a_random_mutil = randint(1,10)
    b_random_mutil = randint(1,10)
    a_array_mutil_test.append(a_random_mutil)
    b_array_mutil_test.append(b_random_mutil)

input_test(a_array_mutil_test,b_array_mutil_test,'x')