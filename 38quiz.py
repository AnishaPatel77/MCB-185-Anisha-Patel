# co authors Varsha, Avantika, Francesa, Lisa

def pi_func(iterations):
	total = 1
	sign = -1
	for i in range(3, iterations, 2):
		total = total + sign * (1 / i)
		sign = sign * -1
	return total
	
