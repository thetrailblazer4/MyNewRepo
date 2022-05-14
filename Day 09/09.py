import logging
logging.basicConfig(filename='demo.log', level=logging.INFO)

def logger(func):
	def log_func(*args):
		logging.info(f"Excuted {func.__name__} with args {args}")
		print(func(*args))
	return log_func

@logger
def add(x,y):
	return x + y 

def sub(x,y):
	return x - y 

@logger
def addition(x,y,z):
	return x +y + z

@logger
def sqaure(x):
	return x * x

sqaure(5)