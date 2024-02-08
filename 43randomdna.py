# 43randomdna.py by Anisha Patel & Varsha Thalladi

import random 

for i in range(3):
	print(f'>seq-{i + 1}')
	for i in range(random.randint(50, 60)):
		print(random.choice('ACGT'), end='')
	print()
 