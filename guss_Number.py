######################The simple number guessing game ######################
###############################by - payakan############################



import random

num = random.randint(0,100)

life = 5

def easy():
	"""It's just like same simple guessing number and in this method having 10 chances so it's easy"""
	global life 
	life =10
	print(f'You have {life} chances')
	while True:
		if life ==0:
			print('\nYOU LOSE\n')
			print(f'The correct answer is {num}')
			exit()
		guessed_num = int(input("Enter the guessed number between 1 - 100 : "))
		

		if num < guessed_num:
			print('Too high')
			life -=1
			print(f'You have only {life} chances')

		elif num > guessed_num:
			print('Too low')
			life -= 1
			print(f'You have only {life} chances')
		elif num == guessed_num:
			print('\nYOU GOT IT!\n')
			print(f'The correct number is {num}')
			break

def hard():
	"""It's just like same simple guessing number and in this method having 5 chances so it's hard """
	global life
	print(f'You have {life} chances')
	while True:
		if life ==0:
			print('\nYOU LOSE\n')
			print(f'The correct number is {num}') 
			exit()
		guessed_num = int(input("Enter th guessed number between 1 - 100 : "))
		

		if num < guessed_num:
			print('Too high')
			life -=1
			print(f'You have only {life} chances')

		elif num > guessed_num:
			print('Too low')
			life -= 1
			print(f'You have only {life} chances')
		elif num == guessed_num:
			print('\nYOU GOT IT!\n')
			print(f'The correct number is {num}') 
			break

hore = input('Enter the difficulty level of your game. type hard or h either easy or e :\n ')
hore = hore.lower()
if hore == 'h' or hore == 'hard':
	hard()
elif hore == 'e' or hore == 'easy':
	easy()
else:
	print('You Enter The Wrong Key')
	
