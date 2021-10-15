print("Let's play blackjack")
from blj_funcs import reform, draw, busted_chec
import random
import os
def clear(): os.system('cls') #on Windows System

# Basic parameters
cards_=[11,2,3,4,5,6,7,8,9,10,10,10,10]
play=True
player_wins=0
dealer_wins=0
draws=0


while play:
    under_17=True
    busted=False
    dealer=[]
    player=random.choices(cards_,k=2)
    dealer=[random.choice(cards_)]

    if sum(player)==21:
        print('You got blackjack')
        player_wins+=1
        continue
    print(f'You hand  is {reform(player)} with sum {sum(reform(player))}')   # Reform function, reforms card in case that there ia an ace in player's hand
    print(f'Dealers hand is {dealer}')
    player=reform(player)
    again=True
    while again:
        hit=input('Will you hit? yes or no\n').lower()
        if hit[0]=='y':
            player=draw(player)
            player=reform(player)
            if busted_chec(player):
                print(f'You are busted with {player} with sum of {sum(player)} sorry!')
                dealer_wins+=1
                under_17=False
                busted=True
                break
            print(f'Your hand is {player} sum is {sum(player)}')
            print(f"Dealer's hand is {dealer}")
            if sum(player)==21:
                print('You won with 21')
                player_wins+=1
                under_17=False
                break
        elif hit[0]=='n':
            break 
        else:
            print('Pelase give a clear order!')
            continue
    
    while under_17:
        dealer=draw(dealer)
        dealer=reform(dealer)
        if busted_chec(dealer):
            print(f'Dealer is busted with {dealer} with sum of {sum(dealer)} you win!')
            player_wins+=1
            busted=True
            break
        if sum(dealer)>16:
            print(f'Dealer stops at {sum(dealer)}')
            under_17=False
        
    while not busted:
        if sum(player)>sum(dealer):
            print('You win')
            player_wins+=1
            break
        elif sum(player)<sum(dealer):
            print('Dealer wins')
            dealer_wins+=1
            break
        else:
            print('it is a draw')
            draws+=1
            break
    
    play_again=input('Will you play again? yes or no').lower()
    if play_again[0]=='n':
        play=False
    clear()
print(f'Final resules are\nPlayer wins {player_wins} times\nDealer wins {dealer_wins} times\nWe had {draws} draws')
    








    

