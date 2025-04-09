import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerschoice = input('\nEnter ... \n1 for rock, \n2 for paper,\n3 for sissors\n\n')

    if playerschoice not in ['1','2','3']:
        print('you must enter 1, 2, or 3\n')
        return play_rps()

    player = int(playerschoice)

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('\nyou chose ' + str(RPS(player)).replace('RPS.', '') + '.')
    print('python chose ' + str(RPS(computer)).replace('RPS.', '') + '.')

    if player == 1 and computer == 3:
        print('🎉 you win')
    elif player == 2 and computer == 1:
        print('🎉 you win')
    elif player == 3 and computer == 2:
        print('🎉 you win')
    elif player == computer:
        print('😲 tie game')
    else:
        print('🐍 python wins')

    while True:
        playagain = input('\nplay again? \nY for yes or \nQ for quit\n')
        if playagain.lower() not in ['y','q']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        return play_rps()
    else:
        print('\n🎉🎉🎉🎉🎉')
        print('thanks for playing\n')
        sys.exit('bye')



play_rps()