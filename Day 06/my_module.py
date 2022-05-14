def find_index(to_search, target):
	for index, value in enumerate(to_search):
		if value == target:
			return index
	return 'Not found!'

new_var = 'hello world'