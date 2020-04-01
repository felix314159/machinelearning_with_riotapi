from __future__ import print_function
import pandas as pd
import numpy as np
from IPython.display import HTML
import keras
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM, RNN, SimpleRNNCell, SimpleRNN
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


class SampleResult(keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):

        start_index = random.randint(0, len(text) - maxlen - 1)

        for diversity in [0.4, 0.6, 0.8, 1.0, 1.2, 1.4]:
            generated = ''
            sentence = text[start_index: start_index + maxlen]
            generated += sentence
            print()
            print('----- Generating with diversity',
                  diversity, 'seed: "' + sentence + '"')
            sys.stdout.write(generated)


            for i in range(100):
                x = np.zeros((1, maxlen, len(chars)))
                for t, char in enumerate(sentence):
                    x[0, t, char_indices[char]] = 1.

                preds = self.model.predict(x, verbose=0)[0]
                next_index = sample(preds, diversity)
                next_char = indices_char[next_index]

                generated += next_char
                sentence = sentence[1:] + next_char

                



                

                sys.stdout.write(next_char)
                




                sys.stdout.flush()
        print('\n\n')




companies = pd.read_csv('./dataset.csv', header=None)
companies.head()

names = companies[0].values
text = '\n'.join(names)

chars = sorted(list(set(text)))
print('total chars: {}'.format(len(chars)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print('Corpus length:', len(text), 'lines:', len(names))
print('First 10 lines:', names[:10])
print('Number of unique chars:', len(chars))


maxlen = 10
step = 3

sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('Number of sequences:', len(sentences))
print('First 10 sequences and next chars:')
for i in range(10):
    print('[{}]:[{}]'.format(sentences[i], next_chars[i]))


print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
print('Size of X: {:.2f} MB'.format(X.nbytes/1024/1024))
print('Size of y: {:.2f} MB'.format(y.nbytes/1024/1024))



nb_units = 64
model = Sequential()
model.add(LSTM(nb_units, input_shape=(maxlen, len(chars))))
model.add(Dense(units=len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy',
              optimizer=optimizer)
print(model.summary())

sample_callback = SampleResult()

history = model.fit(X, y, 
                        epochs=100, 
                        batch_size=512,
                        verbose=2,
                       callbacks=[sample_callback])


model.save('./final_model.h5')
