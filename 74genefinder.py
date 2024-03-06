# 74genefinder.py by Anisha Patel, Varsha, and Lisa 

# python3 74genefinder.py ecoli.fna.gz 300

import sys
import mcb185

def find_orf(seq, min_len):
	stop = ['TAA', 'TAG', 'TGA']
	orfs = []
	i = 0
	
	while i < len(seq) - min_len:
		if seq[i:i+3] == 'ATG':
			for j in range(i+3, len(seq), 3):
				if seq[j:j+3] in stop:
					orf_len = j + 3 - i
					if orf_len >= min_len:
						orfs.append((i, j+3))
						i = j + 3
						break
			else:
				i += 3
				continue
		i += 1
	return orfs
		
def output_gff(orfs, defline, strand):
	for start, end in orfs:
		print(f"{defline}\t.\tCDS\t{start+1}\t{end}\t.\t{strand}\t.\t.")
		
def rev_comp(seq):
	comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	rev_comp_seq = ""
	for i in range(len(seq) -1, -1, -1):
		rev_comp_seq += comp[seq[i]]
	return rev_comp_seq

fasta_file = sys.argv[1]
min_orf = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fasta_file):
	sliced_seq = seq[:10000]
	orfs_forward = find_orf(sliced_seq, min_orf)
	output_gff(orfs_forward, defline, '+')
	
	rev_seq = rev_comp(sliced_seq)
	rev_orf = find_orf(rev_seq, min_orf)
	output_gff(rev_orf, defline, '-')