# Class and Instance variables


# def demo():
# 	pass

class Emp:

	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp_1 = Emp('John', 'M', 60000)
emp_2 = Emp('Jane','K', 70000)

emp_1.raise_amount = 1.02

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)
print(Emp.raise_amount)