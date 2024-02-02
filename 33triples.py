# 33triples.py by Anisha Patel

limit = 100
for i in range(1, limit):
	for j in range(i, limit):
		n = (i ** 2 + j ** 2) ** 0.5
		if n == n // 1:
			print(i, j, n)

