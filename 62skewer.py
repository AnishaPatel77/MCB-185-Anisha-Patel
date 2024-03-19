# 62skewer.py by Anisha Patel, Varsha, & Avantika

# python3 62skewer.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz 1000

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
print(seq)
w = 10

g = seq[0:w].count('G')
c = seq[0:w].count('C')

print(f'0\t{(g + c) / w:.3f}\t{(g - c) / (g + c):.3f}')

for i in range(0, len(seq) - w):
	leaving_nt = seq[i]
	new_nt = seq[i+w]
	if leaving_nt == 'G':
		g -= 1
	elif leaving_nt == 'C':
		c -= 1
		
	if new_nt == 'G':
		g += 1
	elif new_nt == 'C':
		c += 1
		
	if g + c == 0:
		skew = 0
	else:
		skew = (g - c) / (g + c)
	print(f'{i+1}\t{(g + c) / w:.3f}\t{skew:.3f}')
	


