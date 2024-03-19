# 80demo.y by Anisha Patel

print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][3])

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog
	
catalog.append({'Name': name, 'Length': length, 'Sequence': seq, 'Description': desc})

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1
	
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)