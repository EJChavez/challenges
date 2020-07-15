#MRO - Method Resolution Order WHATS FIRST IN LINE

class A:
	num = 10

class B(A):
	pass

class C(A):
	num = 1

class D(B, C):
	pass

#print(D.mro()) #it short circuits when it gets num = 1 at C
#print(D.num)



#inheritance structure
#     A
#   /   \
#  /     \
# B       C
#  \     /
#   \   /
#     D



class X : pass
class Y : pass
class Z : pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass
print(M.mro()) #checks the order where you pass in the parameters