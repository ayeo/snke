from collections import deque

from Cube import *
from Env import Env
from Player import *

from keras.models import Sequential
from keras.layers import Dense

import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

num_episodes = 2000
y = 0.95
eps = 0.2
decay_factor = 0.9

env = Env(SIZE)

model = Sequential()
model.add(Dense(10, input_dim=6, activation='sigmoid'))
model.add(Dense(18, activation='sigmoid'))
model.add(Dense(3, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

memory = deque(maxlen=2000)
l = 1

def learn():
    pass

r_avg_list = []
for i in range(num_episodes):
    s = env.reset()
    eps *= decay_factor
    done = False
    while done == False:
        reshape = np.array(s).reshape(1, 6)
        s0_prediction = model.predict(reshape)
        if np.random.random() > eps:
            a = np.random.randint(0, 2)
        else:
            a = np.argmax(s0_prediction)


        new_s, r, done = env.step(a)
        memory.append((s, a, r, new_s, done))

        if (l % 300 == 0):
            minibatch = random.sample(memory, 300)
            for state, action, reward, next_state, done in minibatch:
                target = reward
                if not done:
                    s1_prediction = model.predict(np.array(next_state).reshape(1, 6))
                    target += y * np.max(s1_prediction)  # add reward from next step to chosen action

                target_f = model.predict(np.array(state).reshape(1, 6))
                target_f[0][action] = target
                model.fit(reshape, target_f, epochs=1, verbose=0)

        s = new_s
        l += 1

        # screen.fill((0, 0, 0))
        # clock.tick(FPS)
        # pygame.event.get()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     s, r, done = env.step(2)
        #     print(s)
        # elif keys[pygame.K_RIGHT]:
        #     s, r, done = env.step(1)
        #     print(s)
        # elif keys[pygame.K_UP]:
        #     s, r, done = env.step(0)
        #     print(s)
        # else:
        #     s, r, done = env.step(0)

        # env.sprites().draw(screen)
        # pygame.display.flip()
        #pygame.time.delay(200)
    r_avg_list.append(env.player.score)


import matplotlib.pyplot as plt

plt.plot(r_avg_list)
plt.show()

pygame.quit()