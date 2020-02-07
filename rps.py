import random

result = dict()
result[('r','r')] = 0
result[('r','p')] = -1
result[('r','s')] = 1
result[('p','r')] = 1
result[('p','p')] = 0
result[('p','s')] = -1
result[('s','r')] = -1
result[('s','p')] = 1
result[('s','s')] = 0

score = []

for game in range(0,5):
    yourChoice = input('Enter your choice (r/p/s): ')
    computerChoice = random.choice('rps')
    try:
        score.append(result[(yourChoice.lower(),computerChoice)])
    except KeyError:
        print('Be careful with your choice')
        score.append(0)
    else:
        print('You seleted {0} and computer {1} so score {2}'.format(yourChoice, computerChoice, score[game]))

print('Your total score is {0}'.format(sum(score)))


	
