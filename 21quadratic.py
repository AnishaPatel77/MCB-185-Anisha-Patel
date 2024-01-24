# 21quadratic.py by Anisha Patel

def quadratic(a, b, c):
	root_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	root_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	return root_1, root_2

print(quadratic(1, 2, 3))
print(quadratic(3, 4, 5))
print(quadratic(2, 4, 5))