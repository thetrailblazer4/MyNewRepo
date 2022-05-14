def decorator_func(original_function):
	def wrapper_func(**kwargs):
		print('Hello world!')
		return original_function(**kwargs)
	return wrapper_func

@decorator_func
def display():
	print('This is a display Function')


@decorator_func
def display_info(name, age):
	print(f"display_info ran with args({name}, {age})")


display_info(name='John', age=26)