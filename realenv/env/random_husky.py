from __future__ import print_function
import time
import numpy as np
import sys
sys.path.append("../env")
from PIL import Image
from simple_env import SimpleEnv
from generate_actions import *
from render.profiler import Profiler


class RandomAgent(object):
    """The world's simplest agent"""
    def __init__(self, action_space):
        self.action_space = action_space
        self.time = 0
        self.repeat = 1
        self.action_last  = None

    def act(self, observation, reward=None):
        if self.time < self.repeat:
            self.time = self.time + 1
            return self.action_last
        else:
            self.time = 0
            action = self.action_space[np.random.randint(0, len(self.action_space))]
            self.action_last = action
            return action


if __name__ == '__main__':
    action_space = generate_actions()
    agent = RandomAgent(action_space)
    env = SimpleEnv(human=False, debug=True)
    ob = None

    i = 0
    try:
        while True:
            if (i <= 14):
                observation, reward = env._step({})
            #elif (i == 10000):
            #    observation, reward = env.reset()
            else:
                action = agent.act(ob)
                with Profiler("Agent step function"):
                    observation, reward = env._step(action)
                print("Husky action", action, "reward %.3f"% reward)
            i = i + 1
            print("current step", i)
            #time.sleep(0.2)

    except KeyboardInterrupt:
        env._end()
        print("Program finished")