import random

answer = input('Write your guess: ')
ourAnswer = random.randint(1, 9)
stopCase = False

while(stopCase == False):
    if (int(answer) == ourAnswer):
        print('Well guessed!')
        stopCase = True
    else:
        answer = input('Bad guess, try again: ')