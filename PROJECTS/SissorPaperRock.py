#created by: Manueldg30
#this code is for a game called "Rock, Paper, Scissors".
#to make it more interesting, we'll create two NPC (Non Playable Character). 
#in the case that the user wants to play with the computer, he can select the option.

import random as r

Main_Player = 0
Non_playable_character = 0

player_name = input("Name: ")
prompt = "\nHi, this is: Rock, paper and Scissors.How do u want to play?"
prompt += "\nAs specter (0) or as player (1): "
prompt1 = "The best of..."
user0 = int(input(prompt))
if user0 != 1 or 0: print("INVALID MODE "), quit()
user1 = int(input(prompt1))
virtual_hand = ["","",""]

if user0 == 1:
    counter0 = 1
    while counter0 <= user1:
        print("---------")
        prompt2 = "What are u going to throw?"
        prompt2 += "\nRock ( ), Paper () or Scissor ( ): "
        player = input(prompt2)
        if player == "scissor":
            print(f"->{player_name}: ")
        elif player == "rock":
            print(f"->{player_name}: ")
        elif player == "paper":
            print(f"->{player_name}: ")
        else:
            print("ERROR ")
        npc1 = r.choice(virtual_hand)
        print(f"->NPC: {npc1}")
        counter0 += 1
elif user0 == 0:
    counter1 = 1
    while counter1 <= user1:
        print("---------")
        npc1 = r.choice(virtual_hand)
        print(f"->NPC 1: {npc1}")
        npc2 = r.choice(virtual_hand)
        print(f"->NPC 2: {npc2}")
        counter1 += 1
else:
    quit()