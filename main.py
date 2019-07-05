from collections import deque

from Agent import DQNAgent
from Cube import *
from Env import Env
from Player import *


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Snke")
clock = pygame.time.Clock()

num_episodes = 1000
y = 0.95
eps = 0.5
decay_factor = 0.9
r_avg_list = []

env = Env(SIZE)

agent = DQNAgent(6, 3)
for e in range(num_episodes):
    state = env.reset()
    state = np.reshape(state, [1, 6])
    done = False
    while not done:
        # turn this on if you want to render
        # env.render()
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, 6])
        agent.remember(state, action, reward, next_state, done)
        agent.priority(state, action, reward, next_state, done)
        state = next_state

        screen.fill((0, 0, 0))
        pygame.event.get()
        clock.tick(FPS)
        env.sprites().draw(screen)
        pygame.display.flip()
        pygame.time.delay(50)
    print("episode: {}/{}, score: {}".format(e, num_episodes, env.player.score))

    r_avg_list.append(env.player.score)
    agent.replay_priority()
    agent.replay(128)

    # done = False
    # env.reset()
    # while not done:
    #     screen.fill((0, 0, 0))
    #     clock.tick(FPS)
    #     pygame.event.get()
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         s, r, done = env.step(2)
    #         print(s)
    #     elif keys[pygame.K_RIGHT]:
    #         s, r, done = env.step(1)
    #         print(s)
    #     elif keys[pygame.K_UP]:
    #         s, r, done = env.step(0)
    #         print(s)
    #     else:
    #         s, r, done = env.step(0)
    #         print(s)
    #
    #     env.sprites().draw(screen)
    #     pygame.display.flip()
    #     pygame.time.delay(200)



import matplotlib.pyplot as plt

plt.plot(r_avg_list)
plt.show()

pygame.quit()