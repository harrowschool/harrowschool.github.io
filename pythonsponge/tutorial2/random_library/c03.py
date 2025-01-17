import random

deck = ['♠1', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠T', '♠J', '♠Q', '♠K', '♠A']

random.shuffle(deck)
print("I shuffled the suit so it's in the order", *deck)

card = random.choice(deck)
print("I took a card at random and it was", card)

cards = random.sample(deck, 4)
print("Then I took four random cards and they were", *cards)
