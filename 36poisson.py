# 36poisson.py by Anisha Patel

# Create a function that computes the Poisson probability of k events 
# occuring with an expectation of n (n^k e^-n / k!) and demonstrate it works 
# by calling it with several values of n and k.

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac