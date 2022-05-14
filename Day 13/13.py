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


class Dev(Emp):
	raise_amount = 1.08

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Emp):
	def __init__(self, first, last, pay, emps=None):
		super().__init__(first, last, pay)
		if emps is None:
			self.emps = []
		else:
			self.emps = emps

	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)

	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)

	def print_emps(self):
		for i in self.emps:
			print(i.fullname())



emp_1 = Dev('John', 'M', 60000, 'Python')
emp_2 = Emp('Jane','K', 60000)
Mgr_1 = Manager('Tom','J', 90000,[emp_1])

# Mgr_1.add_emp(emp_2)

# Mgr_1.remove_emp(emp_1)


# Mgr_1.print_emps()
# print(emp_2.prog_lang)

print(isinstance(Mgr_1, Dev))
print(issubclass(Manager, Emp))