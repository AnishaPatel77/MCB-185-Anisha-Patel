# 44randompi.py by Anisha Patel & Varsha Thalladi

import random
import math

inside = 0 
total = 0 

while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	
	if distance <= 1:
		inside += 1
	total += 1
	
	if total % 100000 == 0:
		print(total, 4 * inside / total)

