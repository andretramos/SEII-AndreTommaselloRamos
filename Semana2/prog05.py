
student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']}
print(student)
print(student['name'])
print(student['courses'])

print(student.get('name'))
print(student.get('phone', 'Not found'))

student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student.get('phone', 'Not found'))
print(student)

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
age = student.pop('age')
print(student)
print(age)

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
	print(key, value) 