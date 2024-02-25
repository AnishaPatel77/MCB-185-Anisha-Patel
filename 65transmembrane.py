# 65transmembrane.py by Anisha Patel, Varsha, & Avantika

# python3 ~/Code/MCB185/src/stylint.py PROGRAM NAME
# python3 65transmembrane.py ../MCB185/data/A.thaliana.fa.gz 100

import sys
import mcb185
import dogma

fasfile = sys.argv[1]
file = mcb185.read_fasta(fasfile)

def kd(seq):
	kd_val = []
	for aa in seq:
		kd_val.append(dogma.Kyte_Doolittle[aa])	
	return kd_val
	
def ave_kd(seq, start, end):
	region = seq[start:end]
	kd_val = kd(region)
	total = 0
	count = 0
	
	for val in kd_val:
		total += val
		count += 1
	
	if count != 0: return total / count
	else: return 0.0
	
def prol(seq, start, end):
	region = ''.join(seq[start:end])
	return 'P' in region

# tm = transmembrane
def tm(file):
	tmprot = []
	for name, seq in file:
		pep_ave_kd = ave_kd(seq, 0, 30)
		tm_ave_kd = ave_kd(seq, 30, 41)
		
		if pep_ave_kd >= 2.5:
			if prol(seq, 0, 30):
				continue
			elif tm_ave_kd >= 0:
				if prol(seq, 30, 41):
					continue
				else:
					tmprot.append((name, seq))
	return tmprot

result = tm(file)
print(result)


			
		