# 56birthday.py by Anisha Patel & Varsha Thalladi

# python3 56birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared_bday = 0

for trial in range(trials):
	calendar = [0] * days
	for i in range(students):
		bday = random.randint(0, days - 1)
		if calendar[bday] == 1:
			shared_bday += 1
			break
		calendar[bday] += 1
		
print(shared_bday / trials)

