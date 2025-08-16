import random

coin = random.choice(["heads", "tails"])
print(coin)


number = random.randint(1, 10)
print(number)


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "A"]
#It shuffles the argument in place. It doesn't return a value
random.shuffle(cards)
for card in cards:
    print(card, end=' ')