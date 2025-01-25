import sys
import random


words = sys.argv[1:]

random.shuffle(words)

rearranged = " ".join(words)

print(rearranged)
