message = 'Hello World'

nmessage = message.replace('World','Universe')

print(message)
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

print("\n")

print(nmessage)
print(nmessage.lower())
print(nmessage.upper())
print(nmessage.count('l'))
print(nmessage.find('World'))
print(nmessage.find('Universe'))

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)

message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

#print(dir(name))
#print(help(str))