# 31fizzbuzz.py by Anisha Patel

for i in range(0, 100):
	if i in range(0, 100, 5) and i in range(0, 100, 3):
		print("FizzBuzz")
	elif i in range(0, 100, 3):
		print("Fizz")
	elif i in range(0, 100, 5): 
		print("Buzz")
	else:
		print(i)