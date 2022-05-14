# def demo(message, name='You'):
# 	return f"{message} {name}"



# print(demo('hello', 'John'))


def emp_info(*args,**kwargs):
	print(args)
	print(kwargs)

emp_info('python','Java', name='John',age='27',email='J@company')