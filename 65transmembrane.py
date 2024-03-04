# 65transmembrane.py by Anisha Patel, Varsha, & Avantika

# python3 65transmembrane.py ecoli.faa.gz

import sys
import mcb185
import dogma

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	success = False
	for i in range(0, 30 -8 + 1):
		signalpeptide = seq[i:i+8]
		signalpeptideavg = 0
		for i in signalpeptide:
			signalpeptideavg += dogma.kyte_doolittle(i)
		signalpeptideavg = signalpeptideavg / 8
		if signalpeptideavg >= 2.5 and 'P' not in signalpeptide:
			for j in range(31, len(seq) - 11 + 1):
				targetregion = seq[j:j+11]
				targetregionavg = 0
				for k in targetregion:
					targetregionavg += dogma.kyte_doolittle(k)
				targetregionavg = targetregionavg / 11
				if targetregionavg >= 2.0 and 'P' not in targetregion:
					success = True
					#print(defline)
					break
		if success == True:
			print(defline)
			break
