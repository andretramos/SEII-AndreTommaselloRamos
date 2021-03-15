courses = ['History','Math','Physics','CompSci']

print(courses)
print(len(courses))
print(courses[3])
print(courses[-1]) #negativo pega de trás pra frente
print(courses[:2])
print(courses[1:])

#courses.append('Art')
#courses.insert(0,'Art')
#print(courses)

courses_2 = ['Art','Education']

#courses.insert(0,courses_2)

courses.extend(courses_2)

#courses.remove('Math')
#courses.pop() #Remove o ultimo valor, e retorna esse valor
#courses.reverse()
#courses.sort()

nums = [1,5,2,4,3]
#nums.sort(reverse=True)
#courses.sort(reverse=True)
print(nums)
print(courses)
print(sorted(nums))
print(sorted(courses))

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Art'))
print('Art' in courses)

print('\n')
for index, course in enumerate(courses, start=1):
	print(index, course)

course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)



#Tuplas
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#uple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)


#Sets - Não ligam pra ordem, jogam duplicadas pra fora
# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
