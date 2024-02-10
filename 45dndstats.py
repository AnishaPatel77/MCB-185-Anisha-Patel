# 45dndstats.py by Anisha Patel & Varsha Thalladi

import random 

limit = 1000

# roll 3D6: roll 3 six-sided dice
sum0 = 0 
for i in range(limit):
	for j in range(3):
		dice = random.randint(1, 6)
		sum0 += dice
print("3D6", sum0 / limit)

# roll 3D6r1: roll 3 six-sided dice, but re-roll any 1s
sum1 = 0
for i in range(limit): 
	for j in range(3):
		dice_r1 = random.randint(1, 6)
		if dice_r1 == 1:
			dice_r1 = random.randint(1, 6) 
		sum1 += dice_r1
print("3D6r1", sum1 / limit)

# roll 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
sum2 = 0
for i in range(limit): 
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: sum2 += d1
		else: sum2 += d2
print("3D6x2", sum2 / limit)

# roll 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
sum3 = 0
min_dice = 7
total = 0 
for i in range(limit):
	for i in range(4):
		dice = random.randint(1, 6)
		total += dice 
		if dice < min_dice:
			min_dice = dice  
	sum3 = total - min_dice
print("4D6d1", sum3 / limit)








