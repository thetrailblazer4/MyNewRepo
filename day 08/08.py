

def decorator_func(original_function):
	def wrapper_func():
		print('Hello world!')
		return original_function()
	return wrapper_func

@decorator_func
def display():
	print('This is a display Function')


@decorator_func
def display_info():
	print('This is a display_info Function')


# disp = decorator_func(display)
# disp()

display()
display_info()

# disp_info = decorator_func(display_info)
# disp_info()
# display_info()


# def sqaure(x):
# 	return x * x

# print(sqaure(4))
# # result = sqaure(4)
# result = sqaure

# print(result.__name__)
# print(result(5))



# def outer_func(args):
# 	# message = args
# 	def inner_func():
# 		print(args)

# 	return inner_func

# # outer_func('hi')

# new_var = outer_func('Hello')
# new_var()

# # print(new_var.__name__)


# list_1 = [1,2,4,6]


# def sqaure(x):
# 	return x*x

# def cube(x):
# 	return x*x*x


# def my_map(func, arg_list):
# 	result = []
# 	for i in list_1:
# 		result.append(func(i))
# 	return result


# print(my_map(sqaure, list_1))
# print(my_map(cube, list_1))

# print(sqaure(list_1))

