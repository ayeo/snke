import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import InputLayer

env = gym.make('NChain-v0')
num_episodes = 1000

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, 5)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(2, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

y = 0.95
eps = 0.5
decay_factor = 0.999

r_avg_list = []
states = np.identity(5)

for i in range(num_episodes):
    s = env.reset()
    eps *= decay_factor
    if i % 100 == 0:
        print("Episode {} of {}".format(i + 1, num_episodes))
    done = False
    r_sum = 0
    while not done:
        s0_prediction = model.predict(states[s:s + 1])
        if np.random.random() < eps:
            a = np.random.randint(0, 2)
        else:
            a = np.argmax(s0_prediction)

        target = s0_prediction
        new_s, r, done, _ = env.step(a)
        s1_prediction = model.predict(states[new_s:new_s + 1])
        target[0][a] = r + y * np.max(s1_prediction) # add reward from next step to chosen action

        model.fit(states[s:s + 1], target, epochs=1, verbose=0)
        s = new_s
        r_sum += r
    r_avg_list.append(r_sum / 1000)


import matplotlib.pyplot as plt

plt.plot(r_avg_list)
plt.show()
