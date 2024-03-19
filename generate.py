import time
import random
import statistics
 
cards = ["queen", "jack", "king"]

random.shuffle(cards)
for card in cards:
    print(card)