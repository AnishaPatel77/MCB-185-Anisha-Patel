# 35nchoosek.py by Anisha Patel

# Create a function that solves "n choose k": n! / k!(n - k)! and 
# demonstrate that it works by calling it multiple times
# with several values of n an k.


def factorial(n):
	if n == 0: 
		return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
	
print(factorial(5))