if True:
	print('Conditional was true')

if False:
	print('Conditional was true')

language = 'Python'

if language == 'Python':
	print('Language is Python')
else: 
	print('no match')


language = 'Java'

if language == 'Python':
	print('Language is Python')
else: 
	print('no match')

language = 'Java'

if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
elif language == 'JavaScript':
	print('Language is JavaScript')
else: 
	print('no match')



user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')


user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = [1,2,3]
b = a

print(a == b)
print(a is b)
print(id(a))
print(id(b))


condition = False

if condition:
	print('True')
else:
	print('False')


condition = None

if condition:
	print('True')
else:
	print('False')


condition = 0

if condition:
	print('True')
else:
	print('False')


condition = ''

if condition:
	print('True')
else:
	print('False')


condition = {}

if condition:
	print('True')
else:
	print('False')