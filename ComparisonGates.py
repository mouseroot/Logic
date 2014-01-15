class ComparisonGates:

	@staticmethod
	def EqualTo(A,B):
		if A == B:
			return True
		return False

	@staticmethod
	def NotEqualTo(A,B):
		if A != B:
			return True
		return False

	@staticmethod
	def GreaterThen(A,B):
		if A > B:
			return True
		return False

	@staticmethod
	def GreaterThenEqualTo(A,B):
		condA = ComparisonGates.GreaterThen(A,B)
		condB = ComparisonGates.EqualTo(A,B)
		if condA or condB:
			return True
		return False

	@staticmethod
	def LessThen(A,B):
		if A < B:
			return True
		return False

	@staticmethod
	def LessThenEqualTo(A,B):
		condA = ComparisonGates.LessThen(A,B)
		condB = ComparisonGates.EqualTo(A,B)
		if condA or condB:
			return True
		return False


if __name__ == "__main__":
	test0 = ComparisonGates.EqualTo(1,1)
	test1 = ComparisonGates.NotEqualTo(1,0)
	test2 = ComparisonGates.GreaterThen(100,1)
	test3 = ComparisonGates.GreaterThenEqualTo(100,100)
	test4 = ComparisonGates.LessThen(1,100)
	test5 = ComparisonGates.LessThenEqualTo(1,1)
	tests = [test0,test1,test2,test3,test4,test5]
	for n,r in enumerate(tests):
		print n,"->",r
