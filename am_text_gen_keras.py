import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from am_process_text import DataGen
from models import *
from training_handler import *

seq_length = 100
batch_size = 5

print("Generating Data")
gen = DataGen("data/small.txt", "data/geez.txt", batch_size, seq_length)
gen.stride = 1
gen.process()
x_dims, y_dims, z_dims = gen.data_dims

input_shape = (x_dims[1], x_dims[2])

class_model = get_class_model(input_shape, y_dims[1])
char_model = get_char_model(input_shape, z_dims[1])


class_trainer = TrainingHandler(gen, class_model, "class_model")
char_trainer = TrainingHandler(gen, class_model, "char_model")


class_trainer.train("512-double", 5000, 50, save_model=True)
char_trainer.train("512-double", 5000, 50, save_model=True)

# show_len = 100 
# start = 200
# gen.gen_input_from_file()
# seed_text = gen.raw_datatset[start:start + seq_length]
# gen_seq = []
# print(gen.raw_datatset[start:start + seq_length])
# print()
# print(gen.raw_datatset[start + seq_length:start + seq_length * 2])
# print()
# seed_text = list(seed_text)
# for sh in range(show_len):

#     seed_int = [gen.char2int[s] for s in seed_text]
#     seedvec = np.array(seed_int, dtype=np.float32).reshape(
#         (1, seq_length, 1)) / 350
#     cs = class_model.predict(seedvec)[0].argmax() * 10
#     cr = char_model.predict(seedvec)[0].argmax()
#     char_int = cs + cr
#     if char_int not in gen.int2char:
#         char_int = 350
#     gen_seq.append(char_int)
#     seed_text.append(gen.int2char[char_int])
#     seed_text = seed_text[1:]

# gen_seq = ''.join([gen.int2char[g] for g in gen_seq])
# print(gen_seq)
