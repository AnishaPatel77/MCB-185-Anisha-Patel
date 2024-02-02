# 36poisson.py by Anisha Patel

def factorial(n):
	if n == 0: 
		return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
	
def poisson(n, k):
	e = 2.7182818284590452353602874713527
	prob = ((n ** k) * (e ** -n)) / factorial(k)
	return prob
	
print(poisson(2, 1))
print(poisson(4, 3))
print(poisson(6, 5))
print(poisson(0, 0))