# 25entropy.py by Anisha Patel

import math 

def Shannon_entropy(a, c, g, t,):
	total = a + c + g + t
	if total <= 0: 
		return("Error total count must be greater than 0")
	if total > 0: 
		P_a = a / total
		P_c = c / total
		P_g = g / total
		P_t = t / total
		entropy_value = -1 * (P_a * math.log2(P_a) + P_c * math.log2(P_c) + P_g * math.log2(P_g) + P_t * math.log2(P_t))
		return entropy_value 
	
print("H =", Shannon_entropy(1, 2, 3, 4)) 
print("H =", Shannon_entropy(23213, 31234, 32454, 42535)) 
print("H =", Shannon_entropy(0, 0, 0, 0)) # example with count being 0
 
