# 25entropy.py by Anisha Patel

import math 

def Shannon_entropy(a, c, g, t,):
	tot = a + c + g + t
	if tot <= 0: 
		return "Error total count must be greater than 0"
	if tot > 0: 
		P_a = (a / tot) * math.log2(a / tot)
		P_c = (c / tot) * math.log2(c / tot)
		P_g = (g / tot) * math.log2(g / tot)
		P_t = (t / tot) * math.log2(t / tot)
		entropy_value = -1 * P_a + P_c + P_g + P_t
		return entropy_value 
	
print("H =", Shannon_entropy(1, 2, 3, 4)) 
print("H =", Shannon_entropy(23213, 31234, 32454, 42535)) 
print("H =", Shannon_entropy(0, 0, 0, 0)) # example with count being 0
 
