# coverage.py by Anisha Patel

# p3 coverage.py 30 5 20

import sys
import random

csize = int(sys.argv[1])
rsize = int(sys.argv[2])
rnum = int(sys.argv[3])

# create empty chromosome
chrom = []
for i in range(csize): 
	chrom.append(0)

# fill up chromosome with reads 
for i in range(rnum):
	pos = random.randint(0, csize - rsize)
	for j in range(rsize):
		chrom[pos + j] += 1
print(chrom)

# minimum coverage
min = rnum
for n in chrom[rsize: -rsize]:
	if n < min: min = n 
print(min)

# window
k = 15
seq = 'ACGTACGTAGAGTCTAGTCGATCCT'
print(seq)
for i in range(0, len(seq) - k + 1, 1):
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (c+g)/k)