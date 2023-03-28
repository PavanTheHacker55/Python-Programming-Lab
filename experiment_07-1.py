# i) Find factorial of a given number

n = int(input("Enter a Number: "))
fact = 1
for x in range(1, n+1):
	fact = fact*x
print("Factorial of",n,"is",fact)


# Alternative....
# i = n
# while i>0:
# 	fact = fact*i
# 	i = i-1
