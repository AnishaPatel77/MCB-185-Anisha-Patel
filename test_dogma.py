import dogma

'''
print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))

print(dogma.translate('ATGTAA')) # should return M*
'''

print(dogma.translate('AATGAAGTTGAGCGTTAAGGTCAAAATAACGCTTAAGGTATTGTTGAATAGGTTTAAGTCCCT'))
# run this ^ 

'''
s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
'''

