# unittesting

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		raise ValueError('Cannot divide by Zero')
	return x / y


# print(add(2,5))


# print(divide(5,2))