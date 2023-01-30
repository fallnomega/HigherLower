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
    # player_guess = 'A'
    if player_guess not in ('A','B'):
        print('Selected neither A nor B, exiting program')
        exit()
    else:
        if player_guess=='A':
            return 0
        else:
            return 1

def compare(player_selection, comparison):
    print(comparison[0])
    print(comparison[1])
    if comparison[0]['follower_count'] > comparison[1]['follower_count']:
        return 0
    else:
        return 1
def initiate_game():
    myList =[]
    for x in range(2):
        myList.append(random.choice(game_date.data))
    return myList

def run_game():
    correct_guesses = 0
    keep_alive = True
    while keep_alive==True:
        round = initiate_game()
        output(round)
        player_choice = guessing()
        correct_answer = compare(player_choice,round)
        print(player_choice)
        print(correct_answer)
        if int(player_choice) != int(correct_answer):
            print("Wrong answer")
            keep_alive=False
        else:
            correct_guesses += 1
            print(f"You guessed correct, wins so far: {correct_guesses}")



    return



print (logo)

run_game()

# print (vs)