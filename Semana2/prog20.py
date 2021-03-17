import os

os.chdir('prog20arquivo')
print(os.getcwd())



try:
	f = open('test_file.txt')
	if f.name == 'test_file.txt':
		raise Exception
	# var = bad_var
except FileNotFoundError as e:
	print('Sorry, this file does not exist!')
	print(e)
except Exception as e:
	# print('Sorry, Something went wrong!')
	print('Error!')

else:
	print(f.read())
	f.close()
finally:
	print("Executing Finally")

