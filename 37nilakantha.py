# 37nilakantha.py by Anisha Patel

def nilakantha(num_iterations):
	est_pi = 3
	sign = 1
	
	for i in range(1, num_iterations):
		math = 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
		est_pi = est_pi + sign * math
		sign = sign * -1
	return est_pi
	
print(nilakantha(10))
print(nilakantha(100))
print(nilakantha(1000))
print(nilakantha(10000))
print(nilakantha(100000))