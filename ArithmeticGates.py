import math
from ComparisonGates import ComparisonGates

class ArithmeticGates:

	@staticmethod
	def Absolute(A):
		return math.fabs(A)

	@staticmethod
	def Add(A,B,others=None):
		if others:
			_sum = (A + B)
			for i in others:
				_sum += i
			return _sum
		return A + B

	@staticmethod
	def And(A,B):
		CondA = ComparisonGates.NotEqualTo(A,0)
		CondB = ComparisonGates.NotEqualTo(B,0)
		if ComparisonGates.EqualTo(CondA,CondB):
			return ArithmeticGates.Add(A,B)
		return 0

	@staticmethod
	def Average(inputs):
		_sum = 0
		for i in inputs:
			_sum += i
		return (_sum / len(inputs))

	@staticmethod
	def Divide(A,B):
		return A / B

	@staticmethod
	def Multiply(A,B):
		return A * B

	@staticmethod
	def Negate(A):
		return A * -1

	@staticmethod
	def Pi():
		return math.Pi

	@staticmethod
	def Subtract(A,B):
		return A - B

	@staticmethod
	def Exponet(A,B):
		return A**B

	@staticmethod
	def Increase(A):
		A += 1
		return A

	@staticmethod
	def Decrease(A):
		A -= 1
		return A

	@staticmethod
	def Log10(A):
		return math.log(A,10)

if __name__ == "__main__":
	print ArithmeticGates.Absolute(-20)
	print ArithmeticGates.Add(1,1,[8,10])
	print ArithmeticGates.And(15,5)
	print ArithmeticGates.Average([20,20])
	print ArithmeticGates.Divide(100,5)
	print ArithmeticGates.Exponet(5,2)
	print ArithmeticGates.Increase(19)
	print ArithmeticGates.Decrease(21)
	print ArithmeticGates.Multiply(10,2)
	print ArithmeticGates.Subtract(22,2)
	print ArithmeticGates.Negate(-20)



