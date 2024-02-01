
def checksum(s):
	n=0 
	for c in s:
		n = n + ord(c)
	return n % 256 
	
def maxchar(s):
	mx = 0 
	for c in s:
		if ord(c) > mx:
			mx = ord(c)
	return mx
			
def minchar(s):
	mn = 255 
	for c in s:
		if ord(c) < mn:
			mn = ord(c)
	return mn
			
name = 'anisha'
print(checksum(name))
print(minchar(name))