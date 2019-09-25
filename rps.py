import random
import numpy as np
from colorama import Fore, Back, Style

game_options=["rock","paper","scissors"]
game = ([['Computer',0],
        ['User',0]])

while(True):
    game[0][1]=random.randint(0,2)
    print(Fore.BLUE + "\nRock=0, paper=1, scissors=2 ? (-1 to exit) :" + Fore.BLACK)
    try:
        game[1][1]=int(input())
    except ValueError:
        print(Fore.RED + "\nOops, that's not a number. Try again" + Fore.BLACK)
        continue
    
    if(game[1][1]==-1):
        break
    elif(game[1][1]>2 or game[1][1]<-1):
        print(Fore.RED + "\nPlease enter 0,1,2 for rock paper or scissors (-1 to exit)" + Fore.BLACK)    
    
    result = game[0][1]-game[1][1]

    if(result==0):
        print(Fore.GREEN + "It's a TIE !!!" + Fore.BLACK)
    elif(np.abs(result)==1):
        label=np.where(game[0][1]>game[1][1],game[0][0],game[1][0])
        print(Fore.MAGENTA + f"{label} wins with {game_options[max(game[0][1],game[1][1])]} over {game_options[min(game[0][1],game[1][1])]}" + Fore.BLACK)
    elif(np.abs(result)==2):
        label=np.where(game[0][1]>game[1][1],game[1][0],game[0][0])
        print(Fore.MAGENTA + f"{label} wins with {game_options[min(game[0][1],game[1][1])]} over {game_options[max(game[0][1],game[1][1])]}" + Fore.BLACK)
