from sys import exit
import random

prompt = "> "

# details for prison cell
print """
	You open your eyes. You are in a garden, trees, flowers, animals all around you.
    There is an apple tree beside you.
    You hear a voice from God:
    'You are my creation, I love you, you can do whatever you want here'.
    'but don't eat the apple from the tree'.
    'What's your name?'
    You yell back:
	
"""

name = raw_input(prompt)

print "	'Thank you! I love you too %s!'" % name
	
def garden_start():	
	print """
	You are walking in the garden.
	You see a snake.
	He said the apple on the tree is really delicious.
	
	What do you do?
	
	1. Chat with the snake.
	2. Ingnor the snake.
	3. Try the apple
	4. Not eating the apple and kill the snake.
	
	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		chatting_with_the_snake()
	elif choice == 2:
		go_away()
	elif choice == 3:
		eatting_apple("Live happily in the garden")
	elif choice == 4:
		won("Live happily in the garden")
	else:
		dead("Confused, you die")	

# details for eatting apple
def eatting_apple():
	print """
	You start feeling guilty.
	You grow confused and frightened.
	You feel as if you're being watched.
	
	What do you do?
	
	1. Hide in the bushes.
	2. Have a conversation with God.
	3. Throw up.
	
	"""

	choice = int(raw_input(prompt))
	
	if choice == 1:
		dead("You are bited by a snake. You are dead.")
	elif choice == 2:
		print "You yell at God : Where are you!"
		print "God say you did something wrong"
		stables()

	elif choice == 3:
		garden_start()
	else:
		dead("Confused, you kill yourself somehow.")

# details for ignor.
def go_away():
	print """
	You leave the garden.
	You saw a prosperous world.
	
	What do you do?
	
	1. Walk into the world.
	2. You desperate to join this world.
	3. Turn back, quickly!
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		print """	You saw people telling lies, being greedy, teasting others
		            You think you need to stop people from doing it.
		"""
		stop_people()

	elif choice == 2:
		stables("You enjoy the sinful life with others, feel confused finally")
	
	else:
		dead("The snake bited you. You died")
	
# details for boat room
def stop_people():
	print """
	You stop people from worshiping other God.
	You warn people to behave.

	What do you do?
	
	1. You pray for the sinful world.
	2. You get used to the sinful world.
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		won("You keep yourself away from sin.")
	elif choice == 2:
		dead("Someone rob and kill you")
	else:
		dead("Confused, you fall into the water and drown.")

# details for stables
def stables():
	print """
	God said He loves you a lot.
	but you need to listen what he said sometimes

	What do you do?
	
	1. You say sorry to God, and you love him as well.
	2. You deny your sin, walk away for God.
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		won("You have a happy life with God after all.")
	elif choice == 2:
		dead("You dead of starvation.")
	
	else:
		dead("Confused, you are bited by the snake")

# details for chat with the snake
def chatting_with_the_snake():
	print """
	You ask the snake why it does this to you.
	He said you can have all the properties in the world.
	
	What you do?
	
	1. You eat the apple.
	2. You killed the snake.
	
	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		eatting_apple()
	elif choice == 2:
		won("You keep away from sin.")

# details for dead function
def dead(why):
	print why, "Separated from God forever %s." % name
	exit(0)
	
# details for won
def won(why):
	print why, "God loves you %s!" % name
	exit(1)
	
garden_start()
