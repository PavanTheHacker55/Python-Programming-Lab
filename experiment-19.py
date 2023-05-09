# Write a Program to Create a package and accessing a package.

# Directory Structure
# -------------------
# C:\
# ---
#   |-->Cars
#  	|	|--> Bmw.py
#   |	|--> Audi.py
#   |	|--> __init__.py
#   |
# 	|-->test
#    	|--> test.py
# --------------------------------------------------------------
# C:\Cars\Bmw.py
# --------------
class Bmw:
	def __init__(self):
		self.models = ['i8', 'x1', 'x5', 'x6']

	def outModels(self):
		print('These are the available models for BMW')
		for model in self.models:
			print(model,end='\t')

# C:\Cars\Audi.py
# ---------------
class Audi:
	def __init__(self):
		self.models = ['q7', 'a6', 'a8', 'a3']

	def outModels(self):
		print('These are the available models for Audi')
		for model in self.models:
			print(model,end='\t')

# C:\Cars\__init__.py
# -------------------
# from Cars import Bmw
# from Cars import Audi

# ------------------------------------------------------------
# C:\Test\main.py
# ---------------
# from Cars import Bmw
# from Cars import Audi
MyBMW = Bmw()
MyBMW.outModels()
print()
MyAudi = Audi()
MyAudi.outModels()