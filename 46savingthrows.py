# 46savingthrows.py by Anisha Patel & Varsha Thalladi

import random

limit = 10000 
fail = 0 
success = 0

def normal_roll(value):
	fail = 0 
	success = 0 
	for i in range(limit):
		roll = random.randint(1, 20)
		if roll >= value: success += 1
		else: fail += 1
	return success / limit
	
print("Normal DC 5:", normal_roll(5))
print("Normal DC 10:", normal_roll(10))
print("Normal DC 15:", normal_roll(15))

def advantage_roll(value):
	fail = 0 
	success = 0 
	for i in range(limit):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 >= value: success += 1
		elif roll2 >= value: success += 1
		else: fail += 1
	return success / limit

print("Advantage DC 5:", advantage_roll(5))
print("Advantage DC 10:", advantage_roll(10))
print("Advantage DC 15:", advantage_roll(15))

def disadvantage_roll(value):
	fail = 0 
	success = 0 
	for i in range(limit):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 <= roll2 and roll1 >= value:
			success += 1
		elif roll2 <= roll1 and roll2 >= value:
			success += 1
		else:
			fail += 1
	return success / limit

print("Disadvantage DC 5:", disadvantage_roll(5))
print("Disadvantage DC 10:", disadvantage_roll(10))
print("Disadvantage DC 15:", disadvantage_roll(15))





