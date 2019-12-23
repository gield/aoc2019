def deal_into_new_stack(deck):
    return deck[::-1]


def cut(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    deck_length = len(deck)
    new_deck = [0] * deck_length
    i = 0
    while deck:
        new_deck[i] = deck.pop(0)
        i = (i + n) % deck_length
    return new_deck

with open("input.txt", "r") as f:
    actions = list(map(str.strip, f.readlines()))

deck = list(range(10007))
for action in actions:
    if action == "deal into new stack":
        deck = deal_into_new_stack(deck)
    else:
        n = int(action.split(" ")[-1])
        if action.startswith("cut"):
            deck = cut(deck, n)
        else:
            deck = deal_with_increment(deck, n)
print(deck.index(2019))
