# 64profinder.py by Anisha Patel, Varsha, & Avantika

# python3 64profinder.py ../MCB185/data/A.thaliana.fa.gz 100

import sys
import mcb185
import dogma

fas = sys.argv[1]
min_len = int(sys.argv[2])

def six_frame_translation(dna):
	proteins = []

	for frame in range(3):
		protein = ''
		for i in range(frame, len(dna) - 2, 3):
			codon = dna[i:i+3]
			protein += dogma.translate(codon)
		proteins.append(protein)

	rev_dna = dogma.revcomp(dna)
	
	for frame in range(3):
		protein = ''
		for i in range(frame, len(rev_dna) - 2, 3):
			codon = rev_dna[i:i+3]
			protein += dogma.translate(codon)
		proteins.append(protein)
	return proteins

output_proteins = []

for name, seq in mcb185.read_fasta(fas):
	
	proteins = six_frame_translation(seq)

	for i in range(len(proteins)):
		protein = proteins[i]
		if len(protein) >= min_len and protein[0] == 'M' and protein[-1] == '*':
			identifier = f'{name}-prot-{i}'
			output_proteins.append((identifier, protein))

for identifier, protein in output_proteins:
    print(f'>{identifier}')
    for i in range(0, len(protein), 60):
        print(protein[i:i+60])

