import random

import game_date
from art import logo,vs
from game_date import data
#compare instagram people and compare which has higher followers based on game_data info

#it keeps going until the user gets it wrong. it gives back how many wins they managed before guessing wrong on this round.

def output(round):
    contestant = ['A','B']
    index = 0
    for x in round:
        print(f"Compare {contestant[index]} :{x['name']}, a {x['description']}, from {x['country']}")
        if index != 1:
            print (vs)
        index+=1
def guessing():
    player_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_guess not in ('A','B'):
        print('Selected neither A nor B, exiting program')
        exit()



def run_game():
    correct_guesses = 0
    keep_alive = True
    round1 = initiate_game()
    output(round1)
    guessing()


    return
def initiate_game():
    myList =[]
    for x in range(2):
        myList.append(random.choice(game_date.data))
    return myList


print (logo)

run_game()

# print (vs)