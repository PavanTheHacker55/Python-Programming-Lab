# (ii) Find the greatest of the three numbers using conditional operators.
a = 10
b = 30
c = 20

if a>b:
	if a>c:
		print("A is Great")
	else:
		print("C is Great")
elif b>a:
	if b>c:
		print("B is Great")
	else:
		print("C is Great")
else:
	print("C is Great")


# Alternative.....
# if a>b and a>c:
# 	print("A is Great")
# elif b>a and b>c:
# 	print("B is Great")
# else:
# 	print("C is Great")
