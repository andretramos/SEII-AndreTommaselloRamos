from prog09arquivo.my_module import find_index, test
#from prog09arquivo.my_module import *
import sys
#sys.path.append(C:\\Users\\André - Kyros\\Documents\\GitHub\\SEII-AndreTommaselloRamos\\Semana2\\prog09arquivo)

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses,'Math')
print(index) 
print(test)

#print(sys.path)


import random

random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)

#import antigravity