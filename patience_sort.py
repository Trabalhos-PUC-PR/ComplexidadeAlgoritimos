class Pile:
    def __init__(self, pile=None):
        if pile is None:
            pile = []
        self.cards = pile

    def add_card(self, card: int) -> bool:
        if len(self.cards) == 0 or self.cards[-1] >= card:
            self.cards.append(card)
            return True
        return False

    def is_empty(self):
        return len(self.cards) == 0

    def lowest_card(self):
        return self.cards[-1]

    def pop_lowest_card(self):
        return self.cards.pop()


def merge_piles(piles):
    result = [piles[0].pop_lowest_card()]
    if piles[0].is_empty():
        piles.pop(0)
    while len(piles) > 0:
        pile = piles[0]
        index = 0
        for p in range(1, len(piles)):
            if piles[p].lowest_card() < pile.lowest_card():
                pile = piles[p]
                index = p
        result.append(pile.pop_lowest_card())
        if pile.is_empty():
            piles.pop(index)
    return result


def patience_sort(x):
    piles = []
    for v in x:
        for pile in piles:
            if pile.add_card(v):
                break
        else:
            piles.append(Pile([v]))
    r = merge_piles(piles)
    return r
