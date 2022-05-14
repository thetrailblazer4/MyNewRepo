# LEGB -- Local --> Enclosing -->Global --> Builtins

# x = 'global x'


# def demo(args):
# 	# global y
# 	y = 'local y'
# 	print(x)
# 	print(args)

# demo('local z')
# print(x)
# # print(y)
# # print(args)


# import builtins


# print(dir(builtins))

# print(help(min))

# def min():
# 	pass

# list_1 = [4,1,2,5,2,7,9]

# result = min(list_1)
# print(result)

x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()