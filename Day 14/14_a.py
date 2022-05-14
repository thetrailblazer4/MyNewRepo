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

	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname()} - {self.email}"


emp_1 = Emp('John', 'M', 60000)

print(repr(emp_1))
print(emp_1)