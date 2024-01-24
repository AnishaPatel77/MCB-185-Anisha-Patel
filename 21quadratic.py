# 21quadratic.py by Anisha Patel

def quadratic(a, b, c):
	x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	return x_1, x_2

print("x-intercepts:", quadratic(1, 2, 3))
print("x-intercepts:", quadratic(3, 4, 5))
print("x-intercepts:", quadratic(2, 4, 5))