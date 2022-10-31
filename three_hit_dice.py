"""
https://www.reddit.com/r/probabilitytheory/comments/jpexpv/probability_in_a_die_rolling_scenario_question/

From kakeguri twin, season 1 episode 1
"""
import random

from collections import Counter, deque


def distribute(trials):
    counter = Counter()
    queue = deque([random.choice("UD") for _ in range(3)])
    for _ in range(trials):
        queue.popleft()
        queue.append(random.choice("UD"))
        counter["".join(queue)] += 1

    for key, value in counter.items():
        counter[key] = value / trials

    return counter


for chain, probability_mass in sorted(distribute(10000).items(), key=lambda p: p[1]):
    print(chain, probability_mass)
