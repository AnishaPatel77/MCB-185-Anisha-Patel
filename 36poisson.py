# 36poisson.py by Anisha Patel

import math 

def factorial(n):
	if n == 0: 
		return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
	
def poisson(n, k):
	prob = ((n ** k) * (math.e ** -n)) / factorial(k)
	return prob
	
print(poisson(2, 1))
print(poisson(4, 3))
print(poisson(6, 5))
print(poisson(0, 0))