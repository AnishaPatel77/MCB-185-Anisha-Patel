# 32fibonacci.py by Anisha Patel

def fibonacci(n):
	num = 0
	nxt_num = 1
	
	for i in range(1, n):
		print(num, end=", ")
		temp_num = num
		num = nxt_num
		nxt_num = nxt_num + temp_num 
	return num

print(fibonacci(10))