class Emp:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

		Emp.num_of_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


# emp_1 = Emp('John', 'M', 60000)
# emp_2 = Emp('Jane','K', 70000)

import datetime

my_date = datetime.date(2022,4,24)
print(my_date)

print(Emp.is_workday(my_date))

# emp_1_str = 'John-M-60000'

# emp_1_new = Emp.from_str(emp_1_str)

# print(emp_1_new.fullname())

# import datetime

# print(datetime.__file__)