#rock scissor paper game
#developed by Abhishek Kumar Bharti
import random
var=['rock','scissor','paper']
count = 0
comp_win = 0
human_win = 0
none = 0
print('\t--------------ROCK,PAPER AND SCISSOR GAME-----------------')
print('\t------------------COMPUTER VS HUMAN---------------------')
print('Developed by Abhishek Bharti\n')
while (count < 10):              #no of round of match
	r= random.choice(var)
	data=input('what you want to choose(rock,scissor,paper):- ')
	if 'rock' in data and 'rock' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('Match draw')
		none = none +1
	elif 'rock' in data and 'scissor' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you win')
		human_win = human_win +1
	elif 'rock' in data and 'paper' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you loose')
		comp_win = comp_win +1
	elif 'scissor' in data and 'rock' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you loose')	
		comp_win = comp_win +1
	elif 'scissor' in data and 'scissor' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('Match draw')	
		none = none +1
	elif 'scissor' in data and 'paper' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you win')
		human_win = human_win +1	
	elif 'paper' in data and 'rock' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you win')
		human_win = human_win +1	
	elif 'paper' in data and 'scissor' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('you loose')	
		comp_win = comp_win +1
	elif 'paper' in data and 'paper' in r:
		print('you have choosed',format(data))
		print('computer choosed',format(r))
		print('match draw')
		none = none +1	
	count = count +1

print(f'No. of match draw {none}')
print(f'No. of match computer won is {comp_win}')
print(f'No. of match you win is {human_win}')
if comp_win > human_win:
	print('\t\t---------- YOU LOOSE ----------')
elif human_win > comp_win:
	print('\t\t---------- YOU WIN ------------')
elif human_win == comp_win:
	print('\t\t---------- MATCH DRAW ----------')
