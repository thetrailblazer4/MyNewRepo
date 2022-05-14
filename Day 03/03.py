# # # messages = ['Hello', 'Bye', 'hey']

# # # print('Bye' in message)

# # # for i, v in enumerate(messages):
# # # 	print(i, v)


# # messages = 'Hello - Bye - hey'

# # new_list = messages.split(' - ')

# # new_str = ' | '.join(new_list)
# # print(messages)

# # print(new_list)

# # print(type(new_str))

# # Mutable
# # list_1 = ['Hello', 'Bye', 'hey']
# # list_2 = list_1

# # print(list_1)
# # print(list_2)

# # list_1[0] = 'Hi'

# # print(list_1)
# # print(list_2)

# #Immutable
# # Tuples 
# # tuple_1 = ('Hello', 'Bye', 'hey')
# # tuple_2 = tuple_1

# # print(tuple_1)
# # print(tuple_2)

# # tuple_1[0] = 'Hi'

# # print(tuple_1)
# # print(tuple_2)


# # Sets
# # messages = {'Hello', 'Bye', 'hey', 'Hello', 'hey','Hi', 'Bye'}

# # print(messages)

# # print('Hey' in messages)


# # # Empty Lists
# # empty_list = []
# # empty_list = list()

# # # Empty tuples
# # empty_tuple = ()
# # empty_tuple = tuple()

# # # Empty Set
# # empty_set = {}    # This is used for creating dict
# # empty_set = set()


# # Dict {Key_1:value_1, key_2:value_2}

# emp_info = {'name':'John','age':27,'prog_lang':['Python','Java']}

# # print(emp_info.keys())
# # print(emp_info.values())
# # print(emp_info.items())

# for i,v in emp_info.items():
# 	print(f"{i} - {v} ")


# # emp_info['phone'] = '4444-44555'
# # emp_info['email'] = 'j@company.com'

# # emp_info.update({'phone':'4444-5555', 'email':'j@company.com'})

# # del emp_info['age']

# # emp_info.pop('age')

# # print(emp_info)
# # print(emp_info.get('phone'))