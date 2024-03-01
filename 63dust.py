# 63dust.py by Anisha Patel, Varsha, & Avantika

# python3 63dust.py ecoli.fna.gz 20 1.4

import sys 
import math
import mcb185

fas = sys.argv[1]
w = int(sys.argv[2])
ent = float(sys.argv[3])

def entropy(seq):
	hval = 0.0
	total = len(seq)
	a = seq.count('A') / total
	c = seq.count('C') / total
	g = seq.count('G') / total
	t = seq.count('T') / total
	
	for base in [a, c, g, t]:
		if base != 0:
			hval -= base * math.log2(base)
	return hval
	
for name, seq in mcb185.read_fasta(fas):
	
	seq = seq[:200]
	dust = list(seq)
	
	for i in range(len(seq) - w + 1):
		dna = seq[i:i+w]
		hval = entropy(dna)
		if hval < ent:
			for j in range(i, i + w):
				dust[j] = 'N'
		
	print('>', name, sep='')
	seq = ''.join(dust)
		
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])