# 65transmembrane.py by Anisha Patel, Varsha, & Avantika

# python3 65transmembrane.py ecoli.faa.gz

import sys
import mcb185
import dogma

def transmembrane(file):  
	for defline, seq in mcb185.read_fasta(file):
		success = False
		for i in range(0, 30 -8 + 1):
			signal_peptide = seq[i:i+8]
			signal_peptide_avg = 0
			for i in signal_peptide:
				signal_peptide_avg += dogma.kyte_doolittle(i)
			signal_peptide_avg = signal_peptide_avg / 8
			if signal_peptide_avg >= 2.5 and 'P' not in signal_peptide:
				for j in range(31, len(seq) - 11 + 1):
					target_region = seq[j:j+11]
					target_region_avg = 0
					for k in target_region:
						target_region_avg += dogma.kyte_doolittle(k)
					target_region_avg = target_region_avg / 11
					if target_region_avg >= 2.0 and 'P' not in target_region:
						success = True
						break
			if success == True:
				print(defline)
				break

transmembrane(sys.argv[1])  