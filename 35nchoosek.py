# 35nchoosek.py by Anisha Patel

def factorial(n):
	if n == 0: 
		return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	if n == 0 and k == 0: 
		return 1
	if n <= k:
		return 0
	if n > 0 and k > 0: 
		return factorial(n) / (factorial(k) * factorial(n - k))		

print(nchoosek(4, 2))
print(nchoosek(4, 3))
print(nchoosek(6, 5))
print(nchoosek(0, 0))


