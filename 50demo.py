# 50demo.py by Anisha Patel

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
    
s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ

print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax) # note the parentheses in the output

print(tax[0])      # index
print(tax[::-1])   # slice

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
    
x1, x2 = quadratic(5, 6, 1)          # unpacked tuple - yes
print(x1, x2)                        # pretty
intercepts = quadratic(5, 6, 1)      # packed tuple - no
print(intercepts[0], intercepts[1])  # ugly

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
    
for i, nt in enumerate(nts):
	print(i, nt)
    
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)
    
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)


