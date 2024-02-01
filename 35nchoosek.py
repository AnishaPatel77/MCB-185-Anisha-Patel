# 35nchoosek.py by Anisha Patel

# n! / k!(n - k)!


def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	if n == 0 and k == 0: 
		return 1
	if n > 0 and k > 0: 
		return (n * factorial(n)) / (factorial(k)) * factorial(n - k)		

	
print(nchoosek(1, 2))
print(nchoosek(3, 4))
print(nchoosek(5, 6))
