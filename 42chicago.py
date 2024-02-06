import random 

games = 10
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')
			
games = 1000
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score) # final game score
	
