# 64profinder.py by Anisha Patel, Varsha, & Avantika

# python3 64profinder.py ecoli.fna.gz 100

import sys
import mcb185
import dogma

fas = sys.argv[1]
min_len = int(sys.argv[2])

def find_proteins(trans_seq, min_len):
	valid_proteins = []
	protein = ''
	start_found = False

	for aa in trans_seq:
		if aa == 'M' and not start_found:
			start_found = True
			protein += aa
		elif start_found:
			protein += aa
			if aa == '*':
				if len(protein) >= min_len:
					valid_proteins.append(protein)
				protein = ''
				start_found = False
	return valid_proteins

def six_frame_translation(dna, min_len):
	proteins = []
	frames = [dna, dogma.revcomp(dna)]  

	for dna_seq in frames:
		for frame in range(3):
			trans_seq = dogma.translate(dna_seq[frame:])
			proteins += find_proteins(trans_seq, min_len)
	return proteins

output_proteins = []
for name, seq in mcb185.read_fasta(fas):
	proteins = six_frame_translation(seq, min_len)
	for i, protein in enumerate(proteins):
		identifier = f'{name}-prot-{i}'
		output_proteins.append((identifier, protein))

for identifier, protein in output_proteins:
	print(f'>{identifier}')
	for i in range(0, len(protein), 60):
		print(protein[i:i+60])

