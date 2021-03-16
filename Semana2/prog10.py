import os
from datetime import datetime

#print(dir(os))
'''Printa todos os atributos e métodos disponíveis nesse módulo'''

print(os.getcwd())
os.chdir('../../../..')
os.chdir('Desktop')

#os.mkdir tbm faz a msm coisa, mas não faz diretórios intermediarios

os.makedirs('Ex/Ex')

os.removedirs('Ex/Ex')

#os.rename('test.txt','demo.txt')

mod_time = os.stat('Spotify.lnk').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

print(os.environ.get('HOME'))

#file_path = os.environ.get('HOME') = 'text.txt'
#print(file_path)
#print(os.listdir())
