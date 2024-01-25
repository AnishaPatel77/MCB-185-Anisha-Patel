# 21quadratic.py by Anisha Patel

def quadratic(a, b, c):
	discriminant = (b ** 2 - 4 * a * c)
	if discriminant < 0:
		return "no real solution"
	if discriminant == 0:
		x_1 = (-b + (discriminant ** 0.5)) / (2 * a)
		return x_1
	if discriminant > 0:
		x_1 = (-b + (discriminant ** 0.5)) / (2 * a)
		x_2 = (-b - (discriminant ** 0.5)) / (2 * a)
		return x_1, x_2

print("x-intercept(s):", quadratic(-1, -2, -3)) # no real solution
print("x-intercept(s):", quadratic(1, 2, 1)) # one root
print("x-intercept(s):", quadratic(2, 40, 5)) # two roots 