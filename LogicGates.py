class LogicGates:

	@staticmethod
	def And(A,B):
		if A == 1 and B == 1:
			return 1
		else:
			return 0

	@staticmethod
	def Or(A,B):
		if A == 1 or B == 1:
			return 1
		elif A == 0 and B == 0:
			return 0

	@staticmethod
	def Nor(A,B):
		A = LogicGates.NOT(A)
		B = LogicGates.NOT(B)
		if A == 1 or B == 1:
			return 1
		elif A == 0 and B == 0:
			return 0

	@staticmethod
	def Nand(A,B):
		A = LogicGates.NOT(A)
		B = LogicGates.NOT(B)
		if A == 1 and B == 1:
			return 0
		elif A == 0 or B == 0:
			return 1

	@staticmethod
	def Xor(A,B):
		if A == 1 and B == 0 or A == 0 and B == 1:
			return 1
		if A == 0 and B == 0:
			return 0
		if A == 1 and B == 1:
			return 0

	@staticmethod
	def Not(A):
		if A == 1:
			return 0
		elif A == 0:
			return 1

# def HalfAdder(A,B):
# 	S = LogicGates.XOR(A,B)
# 	C = LogicGates.AND(A,B)
# 	return (S,C)

# def FullAdder(A,B,C):
# 	ha0 = HalfAdder(A,B)
# 	ha1 = HalfAdder(ha0[0],C)
# 	res = LogicGates.OR(ha0[1],ha1[1])
# 	return (res,ha1[1])


def main():
	print "Logic Gates test"
	result0 = LogicGates.Or(1,0)
	result1 = LogicGates.And(1,1)
	result2 = LogicGates.Not(0)
	result3 = LogicGates.Nand(1,0)
	result4 = LogicGates.Nor(0,0)
	result5 = LogicGates.Xor(1,0)
	print "Results:"
	for k,v in enumerate([result0,result1,result2,result3,result4,result5]):
		print "Test %d" % k,"->",v == True
main()