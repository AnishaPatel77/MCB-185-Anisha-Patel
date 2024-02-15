# 53genomestats.py by Anisha Patel & Varsha Thalladi

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

distance = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			distance.append(end - beg + 1)
				
def count(vals):
	count = 0 
	for val in vals:
		count += 1
	return count 
print('n:', count(distance))

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini 
print('min:', minimum(distance))

def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi
print('max:', maximum(distance))

def mean(vals):
	total = 0 
	for val in vals: total += val
	return total / len(vals)
print('mean:', mean(distance))

def stdv(vals):
	amt = count(vals)
	total = 0 
	sqd = 0 
	
	for val in vals:
		total += val
		
	mean_val = total / amt
	
	for val in vals:
		sqd += (val - mean_val) ** 2
	return(sqd / amt) ** 0.5
print('stdv:', stdv(distance))

def median(vals):
	vals.sort()
	n = len(vals)
	middle = n // 2
	
	if n % 2 == 0:
		med = (vals[middle - 1] + vals[middle]) / 2
	else:
		med = vals[middle]
	return med 
print('med:', median(distance))