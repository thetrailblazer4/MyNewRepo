# f = open('demo.log', 'r')

# print(f.read())

# f.close()
# print(f.closed)


# with open('demo.log', 'r') as f:
# 	for line in f:
# 		print(line, end='')

# with open('demo.txt', 'w') as f:
# 	f.write('This is a demo file')
# 	f.seek(0)
# 	f.write('Demo')


# print(f.closed)


with open('demo.log', 'r') as rf:
	with open('demo.txt', 'w') as wf:
		for line in rf:
			wf.write(line)