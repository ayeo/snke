from Cube import *
from Env import Env
from Player import *

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import InputLayer


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

num_episodes = 1000
y = 0.95
eps = 0.5
decay_factor = 0.999

env = Env(SIZE)

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, 6)))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

r_avg_list = []
for i in range(num_episodes):
    s = env.reset()
    eps *= decay_factor
    done = False
    r_sum = 0


    while done == False:
        reshape = np.array(s).reshape(1, 6)
        s0_prediction = model.predict(reshape)
        if np.random.random() < eps:
            a = np.random.randint(0, 2)
        else:
            a = np.argmax(s0_prediction)

        target = s0_prediction
        new_s, r, done = env.step(a)
        reshape1 = np.array(new_s).reshape(1, 6)
        s1_prediction = model.predict(reshape1)
        target[0][a] = r + y * np.max(s1_prediction)  # add reward from next step to chosen action

        model.fit(reshape, target, epochs=1, verbose=0)
        s = new_s
        r_sum += r

        screen.fill((0, 0, 0))
        clock.tick(FPS)
        pygame.event.get()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     s, r, done = env.step(2)
        # elif keys[pygame.K_RIGHT]:
        #     s, r, done = env.step(1)
        # else:
        #     s, r, done = env.step(0)

        env.sprites().draw(screen)
        pygame.display.flip()
        #pygame.time.delay(50)
    r_avg_list.append(r_sum / 1000)


import matplotlib.pyplot as plt

plt.plot(r_avg_list)
plt.show()

pygame.quit()