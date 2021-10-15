cards_=[11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
def busted_chec(cards):
    summary=sum(cards)
    if summary<22:
        return False
    return True

        
def reform(cards):
    for i in cards:
        if i==11 and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return cards

def draw(cards):
    card=random.choice(cards_)
    cards.append(card)
    return cards

