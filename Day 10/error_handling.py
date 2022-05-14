"""try:
	pass
except:
	pass
else:
	pass

FileNotFoundError
NameError

	"""

# print(f)
# f = open('newinfo.csv')

try:
	f = open('newinfo.csv')
	var = new_var
except FileNotFoundError:
	print('Sorry file does not exist')

except Exception:
	print('something went wrong!')

	

