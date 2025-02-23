import sys
import random

num_of_words = int(sys.argv[1])

with open("/usr/share/dict/words") as f:
    lines = f.read().split("\n")

    chosen_words = random.sample(lines, num_of_words)
    sentence = " ".join(chosen_words)
    print(sentence)
