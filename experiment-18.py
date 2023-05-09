# Write a Program to Subtract two complex number using classes and objects.

class Complex:
	def __init__(self, tempReal, tempImaginary):
		self.real = tempReal;
		self.imaginary = tempImaginary;

	def subComp(self, C1, C2):
		temp=Complex(0, 0)
		temp.real = C1.real - C2.real;
		temp.imaginary = C1.imaginary - C2.imaginary;
		return temp;

C1 = Complex(3, 5)
print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))

C2 = Complex(9, 2)
print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))

C3 = Complex(0, 0)
C3 = C3.subComp(C1, C2)
print("Sum of complex number :", C3.real, "+ i"+ str(C3.imaginary))