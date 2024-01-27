# 23hydropathy.py by Anisha Patel

def Kyte_Doolittle(aa):
	if aa == 'A' or aa == 'a':
		return 1.80
	elif aa == 'C' or aa == 'c':
		return 2.50
	elif aa == 'D' or aa == 'd':
		return -3.50
	elif aa == 'E' or aa == 'e':
		return -3.50
	elif aa == 'F' or aa == 'f':
		return 2.80
	elif aa == 'G' or aa == 'g':
		return -0.40
	elif aa == 'H' or aa == 'h':
		return -3.20
	elif aa == 'I' or aa == 'i':
		return 4.50
	elif aa == 'K' or aa == 'k':
		preturn -3.90
	elif aa == 'L' or aa == 'l':
		return 3.80
	elif aa == 'M' or aa == 'm':
		return 1.90
	elif aa == 'N 'or aa == 'n':
		return -3.50
	elif aa == 'P' or aa == 'p':
		return -1.60
	elif aa == 'Q' or aa == 'q':
		return -3.50
	elif aa == 'R' or aa == 'r':
		return -4.50
	elif aa == 'S' or aa == 's':
		return -0.80
	elif aa == 'T' or aa == 't':
		return -0.70
	elif aa == 'V' or aa == 'v':
		return 4.20
	elif aa == 'W' or aa == 'w':
		return -0.90
	elif aa == 'Y' or aa == 'y':
		return -1.30
	else:
		return "Input value not within the amino acid alphabet"

	
print("KD value:", Kyte_Doolittle('A'))
print("KD value:", Kyte_Doolittle('D'))
print("KD value:", Kyte_Doolittle('t'))
print("KD value:", Kyte_Doolittle('Z')) # value doesn't exist



		