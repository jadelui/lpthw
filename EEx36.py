from sys import exit
import random

prompt = "> "

# details for prison cell
print """
	You open your eyes. You are in a garden, trees, flowers, animals all around you.
    There is an apple tree beside you.
    You hear a voice from God:
    ‘You are my creation, I love you, you can do whatever you want here’
    ‘but don’t eat the apple from the tree’
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
	2. Ignore the snake.
	3. Try the apple.
	4. Not eating the apple and kill the snake.
	
	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		chatting_with_the_snake()
	elif choice == 2:
		go_away()
	elif choice == 3:
		eatting_apple()
	elif choice == 4:
		won("Live happily in the garden.")
	else:
		dead("Confused, you die")	

# details for Try the apple
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
		intelligence = random.randint(1,6)
		print "God say you did something wrong %s." % intelligence
		
		if intelligence > 3:
			print "You say sorry to God."
			print "Your relationship with God is being better"
			stables()
		else:
			dead("You deny it is your fault. You run out of the garden, you die of starvation.")
	elif choice == 3:
		garden_start()
	else:
		dead("Confused, you kill yourself somehow.")

# details for guard room, first left
def go_away():
	print """
	You leave the garden.
	You saw a sinful world.
	
	What do you do?
	
	1. Go into the sinful world
	2. Cry 
	3. Turn back, quickly!
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		print "You saw people telling lies, being greedy, teasting others"
		strength = random.randint(1,6)
		print "	You do not know how to deal with these people %s." % strength
		if strength > 3:
			print """
			You think you need to stop people from doing it.

			"""
			stop_people()
		else:
			dead("	You enjoy the sinful life with others, got punished by God")
	elif choice == 2:
		dead("The snake bited you. You died")
	elif choice == 3:
		garden_start()
	else:
		dead("Confused, you die.")
	
# details for stop people
def stop_people():
	print """
	You stop people from worshiping other God.
	You warn people to behave.
	
	What do you do?
	
	1. You pray for the sinful world.
	2. You get used to the sinful world .

	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		won("You keep yourself away from sin.")
	elif choice == 2:
		dead("Someone rob and killed you")
	
	else:
		dead("Confused, you fall into a lake and drown.")

# details for stables
def stables():
	print """
	God said He loves you a lot 
	but you need to listen what he said sometimes
	
	What do you do?
	
	1. You love him as well, you agree.
	2. You walk away from God.
	3. Turn back.
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		won("You have a happy life with God after all.")
	elif choice == 2:
		dead("You dead of starvation.")
	elif choice == 3:
		dead("The snake bite you.")
	else:
		dead("Confused, you are kicked in the head by a horse and killed.")

# details for dark room
def chatting_with_the_snake():
	print """
	You ask the snake why do this to you.
	He said you can have all the properties in the world
	
	What do you do?
	
	1. You killed the snake.
	2. You eat the apple.
	3. Turn back.
	
	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		won("You keep yourself away from sin.")
	elif choice == 2:
		stables()
	elif choice == 3:
		garden_start()
	else:
		dead("Confused, you fall into a lake and drown.")
	

# details for dead function
def dead(why):
	print why, "Separate from God forever %s." % name
	exit(0)
	
# details for escape
def won(why):
	print why, "Congratulations %s!" % name
	exit(1)
	
garden_start()
