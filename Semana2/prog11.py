#File objects
import os

#Mudando de diretório pra manter o git organizado
os.chdir('prog11arquivo')
print(os.getcwd())
print(os.listdir())

f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()
#Não pode esquecer de fechar

with open('test.txt', 'r') as rf:
	'''Esses blocos fecham o arquivo automaticamente
	no fim dessa indentação'''
	'''
	f_contents = f.read()
	print(f_contents)
	f_contents = f.readlines()
	print(f_contents)
	f_contents = f.readline()
	print(f_contents)

	for line in f:
		print(line,end = '')


	f_contents = f.read(100)
	print(f_contents, end = '')

	f_contents = f.read(100)
	print(f_contents, end = '')
	

	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')

	
	while len(f_contents) > 0:
		print(f_contents, end = '')
		f_contents = f.read(size_to_read)
	

	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')

	print(f.tell())
	

	f.write('Test')
	f.seek(0)
	f.write('R')
	'''
	with open('testcopy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)



