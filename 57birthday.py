# 57birthday.py by Anisha Patel, Varsha Thalladi, & Lisa Yuan

# python3 57birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def bday_calendar(trials, days, people):
	shared_bday_trials = 0 
	for i in range(trials):
		calendar = []
		for j in range(days):
			calendar.append(0)
	
		for j in range(people):
			bday = random.randint(0, days - 1)
			calendar[bday] += 1
	
		shared_bday = False
		for day_count in calendar:
			if day_count > 1:
				shared_bday = True
				break
				
		if shared_bday:
			shared_bday_trials += 1
			
	prob = shared_bday_trials / trials * 100
	return prob

print(bday_calendar(trials, days, people), "%")
