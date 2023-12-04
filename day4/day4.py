import re

def a(filepath):
    points = 0
    with open(filepath, "r") as fp:
        for line in fp.readlines():
            _, winnings, haves = re.split(r':|\|', line, maxsplit=2)
            if matches := len(set(winnings.strip().split()).intersection(set(haves.strip().split()))):
                points += 2 ** (matches - 1)
    return points


def b(filepath):
    cards = dict()
    with open(filepath, "r") as fp:
        for line in fp.readlines():
            card, winnings, haves = re.match(r'Card\W+(\d+):(.*)\|(.*)', line).groups()
            card = int(card)

            cards[card] = cards.get(card, 0) + 1
            
            if matches := len(set(winnings.strip().split()).intersection(set(haves.strip().split()))):
                for winCard in range(card + 1, card + 1 + matches):
                    cards[winCard] = cards.get(winCard, 0) + 1 * cards[card]
                
    return sum(cards.values())

print(a("test.txt"))
print(a("input.txt"))
print(b("test.txt"))
print(b("input.txt"))