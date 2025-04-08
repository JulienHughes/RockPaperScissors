import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print('')
    playerschoice = input('Enter ... \n1 for rock, \n2 for paper,\n3 for sissors\n\n')

    player = int(playerschoice)

    if player < 1 or player > 3:
        sys.exit('you must enter 1, 2, or 3\n')

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('')

    print('you chose ' + str(RPS(player)).replace('RPS.', '') + '.')
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
    print('')
    playagain = input('\nplay again? \nY for yes or \nQ for quit\n\n')

    if playagain.lower() == 'y':
        continue
    else:
        print('thanks for playing')
        break

sys.exit('bye')
print('')