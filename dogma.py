def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG':
			aas.append('M')
		elif codon in ['TAA', 'TAG', 'TGA']:
			aas.append('*')
		elif codon in ['TTT', 'TTC']:
			aas.append('F')
		elif codon in ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']:
			aas.append('L')
		elif codon in ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']:
			aas.append('S')
		elif codon in ['TAT', 'TAC']:
			aas.append('Y')
		elif codon in ['TGT', 'TGC']:
			aas.append('C')
		elif codon in ['TGG']:
			aas.append('W')
		elif codon in ['CCT', 'CCC', 'CCA', 'CCG']:
			aas.append('P')
		elif codon in ['CAT', 'CAC']:
			aas.append('H')
		elif codon in ['CAA', 'CAG']:
			aas.append('Q')
		elif codon in ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
			aas.append('R')
		elif codon in ['ATT', 'ATC', 'ATA']:
			aas.append('I')
		elif codon in ['ACT', 'ACC', 'ACA', 'ACG']:
			aas.append('T')
		elif codon in ['AAT', 'AAC']:
			aas.append('N')
		elif codon in ['AAA', 'AAG']:
			aas.append('K')
		elif codon in ['GTT', 'GTC', 'GTA', 'GTG']:
			aas.append('V')
		elif codon in ['GCT', 'GCC', 'GCA', 'GCG']:
			aas.append('A')
		elif codon in ['GAT', 'GAC']:
			aas.append('D')
		elif codon in ['GAA', 'GAG']:
			aas.append('E')
		elif codon in ['GGT', 'GGC', 'GGA', 'GGG']:
			aas.append('G')
		else:
			aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
def kyte_doolittle(aa):
	if aa == 'A' or aa == 'a':
		return 1.80
	elif aa == 'C' or aa == 'c':
		return 2.50
	elif aa == 'D' or aa == 'd':
		return -3.50
	elif aa == 'E' or aa == 'e':
		return -3.50
	elif aa == 'F' or aa == 'f':
		return 2.80
	elif aa == 'G' or aa == 'g':
		return -0.40
	elif aa == 'H' or aa == 'h':
		return -3.20
	elif aa == 'I' or aa == 'i':
		return 4.50
	elif aa == 'K' or aa == 'k':
		return -3.90
	elif aa == 'L' or aa == 'l':
		return 3.80
	elif aa == 'M' or aa == 'm':
		return 1.90
	elif aa == 'N' or aa == 'n':
		return -3.50
	elif aa == 'P' or aa == 'p':
		return -1.60
	elif aa == 'Q' or aa == 'q':
		return -3.50
	elif aa == 'R' or aa == 'r':
		return -4.50
	elif aa == 'S' or aa == 's':
		return -0.80
	elif aa == 'T' or aa == 't':
		return -0.70
	elif aa == 'V' or aa == 'v':
		return 4.20
	elif aa == 'W' or aa == 'w':
		return -0.90
	elif aa == 'Y' or aa == 'y':
		return -1.30
	else:
		return "Input value not within the amino acid alphabet"
		
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)
	
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)

def tm(A, C, G, T):
	oligo = A + C + G + T
	if oligo <= 13:
		melting_temp = (A + T) * 2 + (G + C) * 4
	elif oligo > 13:
		melting_temp = (64.9 + (41 * (G + C - 16.4))) / (A + T + G + C)
	return melting_temp 