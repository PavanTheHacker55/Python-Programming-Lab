# Write a program to: To print Factors of a given Number

def factors(n):
	print("Factors of",n,"are: ")
	for x in range(1, n+1):
		if n % x == 0:
			print(x)

factors(27)