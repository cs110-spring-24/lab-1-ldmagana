import random
cpu=random.randint(1,3)
# 1 is rock, 2 is paper, 3 is scissors

user=input("enter rock, paper, or scissors: ")

if user=="rock":
	if cpu==1: # cpu chose rock
		print("tie game")
	elif cpu=="paper": # cpu chose paper
		print("you lost")
	else: # cpu chose scissors
		print("you win!")

if user=="paper":
	if cpu==1: # cpu chose rock
		print("you lost")
	elif cpu=="paper": # cpu chose paper
		print("tie game")
	else: # cpu chose scissors
		print("you win!")

if user=="scissors":
	if cpu==1: # cpu chose rock
		print("you win!")
	elif cpu=="paper": # cpu chose paper
		print("you lost")
	else: # cpu chose scissors
		print("tie game")
