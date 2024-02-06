# co authors Varsha, Avantika, Francesa, Lisa

def gregory_leibniz(iterations):
	total = 1
	sign = -1
	
	for i in range(1, iterations):
		denominator = 2 * i + 1
		now_add = 1 / denominator
		estimate_pi += sign * now_add
		sign *= -1
	return estimate_pi * 4
	
def nilakantha(iterations):
	est_pi = 3
	sign = 1
	for i in range(1, iterations):
		math = 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
		est_pi = est_pi + sign * math
		sign = sign * -1
	return est_pi

for i in range (1, 100):
	print(gregory_leibniz(i), nilakantha(i))