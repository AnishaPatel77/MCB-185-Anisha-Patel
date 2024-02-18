# 56birthday.py by Anisha Patel & Varsha Thalladi

# python3 56birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared_bday = 0

for trial in range(trials):
	birthday = []
	for i in range(students):
		bday = random.randint(0, days)
		if bday in birthday:
			shared_bday += 1
			break
		birthday.append(bday)
		
print(shared_bday / trials * 100, "%")