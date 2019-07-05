from DQN import DQN
from Cube import *
from Env import Env
from Player import *

env = Env()
agent = DQN(6, 3)

r_avg_list = []
for e in range(EPISODES):
    total_reward = 0
    done = False
    state = np.reshape(env.reset(), [1, 6])
    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, 6])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        env.render()

    print("episode: {}/{}, score: {}, reward: {}".format(e, EPISODES, env.player.score, total_reward))
    r_avg_list.append(env.player.score)
    agent.replay(MINI_BATCH)

    # uncomment to play manually
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

agent.save_mode()
pygame.quit()