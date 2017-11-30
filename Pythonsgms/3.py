from itertools import product
from random import shuffle

cards=list(product(range(1,14),["Hearts","Spades","Clubs","Diamonds"]))
shuffle(cards)
for i in range(0,5):
    print(cards[i])
