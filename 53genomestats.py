# 53genomestats.py by Anisha Patel & Varsha Thalladi

import gzip
import sys


gffpath = sys.argv[1]
feature = sys.argv[2]

'''
count

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

max 

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

standard deviation 

median 
'''
with gzip.open(gffpath, 'rt') as fp:
    for line in fp:
        print(line, end='')
        
# python3 53genometats.py ~/Code/MCB185/data/A.thaliana.gff.gz gene