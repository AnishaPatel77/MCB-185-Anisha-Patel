# 45dndstats.py by Anisha Patel & Varsha Thalladi

import random 

limit = 10 

# roll 3D6: roll 3 six-sided dice
sum0 = 0 
for i in range(limit):
	for j in range(3):
		dice = random.randint(1, 6)
		sum0 += dice
print(sum0 / limit)

# roll 3D6r1: roll 3 six-sided dice, but re-roll any 1s
sum1 = 0
for i in range(limit): 
	for j in range(3):
		dice_r1 = random.randint(1, 6)
		if dice_r1 == 1:
			dice_r1 == random.randint(1, 6) 
		sum1 += dice_r1
print(sum1 / limit)

# roll 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
sum2 = 0
for i in range(limit): 
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: sum2 += d1
		else: sum2 += d2
print(sum2 / limit)

# roll 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
sum3 = 0
for i in range(4):
	for j in range(4):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		
		min_roll = d1
		if d2 < min_roll: min_roll = d2
		if d3 < min_roll: min_roll = d3
		if d4 < min_roll: min_roll = d4
	
		total = 0
		if d1 != min_roll: total += d1
		if d2 != min_roll: total += d2 
		if d3 != min_roll: total += d3 
		if d4 != min_roll: total += d4 
		sum3 += total
print(sum3 / limit)
